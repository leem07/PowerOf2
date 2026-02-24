# my_2048_env.py

import gymnasium as gym
from gymnasium import spaces
import numpy as np


# ==========================================================
# MERGE LOGIC
# ==========================================================

def merge_line(line):
    """Merge a single row/column left. Returns (new_line, score_gained)."""
    tiles = [x for x in line if x != 0]
    merged = []
    score = 0
    i = 0
    while i < len(tiles):
        if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
            val = tiles[i] * 2
            merged.append(val)
            score += val   # Standard 2048: score += merged tile value
            i += 2
        else:
            merged.append(tiles[i])
            i += 1

    while len(merged) < len(line):
        merged.append(0)

    return np.array(merged, dtype=int), score


def move(board, action):
    """Apply an action to the board. Returns new board only (for compatibility)."""
    new_board, _ = move_with_score(board, action)
    return new_board


def move_with_score(board, action):
    """Apply an action. Returns (new_board, score_gained)."""
    board = board.copy()
    total_score = 0

    if action == 0:  # Up
        cols = []
        for col in board.T:
            new_col, s = merge_line(col)
            cols.append(new_col)
            total_score += s
        board = np.array(cols).T

    elif action == 1:  # Down
        cols = []
        for col in board.T:
            new_col, s = merge_line(col[::-1])
            cols.append(new_col[::-1])
            total_score += s
        board = np.array(cols).T

    elif action == 2:  # Left
        rows = []
        for row in board:
            new_row, s = merge_line(row)
            rows.append(new_row)
            total_score += s
        board = np.array(rows)

    elif action == 3:  # Right
        rows = []
        for row in board:
            new_row, s = merge_line(row[::-1])
            rows.append(new_row[::-1])
            total_score += s
        board = np.array(rows)

    return board, total_score


# ==========================================================
# ENVIRONMENT
# ==========================================================

class Game2048Env(gym.Env):

    def __init__(self):
        super().__init__()

        self.board = np.zeros((4, 4), dtype=int)
        self.score = 0

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(
            low=0,
            high=131072,
            shape=(4, 4),
            dtype=np.int32
        )

    # ------------------------------------------------------

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.board = np.zeros((4, 4), dtype=int)
        self.score = 0
        self._add_random_tile()
        self._add_random_tile()

        return self.board.copy(), {}

    # ------------------------------------------------------

    def step(self, action):
        old_board = self.board.copy()
        new_board, merge_score = move_with_score(self.board, action)

        if not np.array_equal(old_board, new_board):
            self.board = new_board
            self.score += merge_score
            self._add_random_tile()
            # Standard reward = points earned this step (merge score)
            reward = float(merge_score)
        else:
            # Illegal move: no change, small penalty
            reward = 0.0

        done = self._is_done()

        return self.board.copy(), reward, done, False, {"score": self.score}

    # ------------------------------------------------------

    def _add_random_tile(self):
        empty = np.argwhere(self.board == 0)
        if len(empty) > 0:
            i, j = empty[np.random.choice(len(empty))]
            self.board[i, j] = 2 if np.random.rand() < 0.9 else 4

    def _is_done(self):
        for action in range(4):
            if not np.array_equal(self.board, move(self.board, action)):
                return False
        return True

    # ------------------------------------------------------

    def render(self, mode="human"):
        print("\n" + "=" * 25)
        for row in self.board:
            print("|" + "|".join(f"{v:5d}" for v in row) + "|")
        print("=" * 25)
        print(f"Max Tile: {self.board.max()}")
        print(f"Score:    {self.score}\n")


# ==========================================================
# REGISTER
# ==========================================================

from gymnasium.envs.registration import register

register(
    id="2048-v0",
    entry_point="my_2048_env:Game2048Env"
)
