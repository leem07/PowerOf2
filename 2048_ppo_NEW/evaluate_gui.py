"""
evaluate_gui.py
---------------
Pygame GUI to watch the PPO agent play 2048.
Score displayed is the standard 2048 score (sum of merged tile values).
"""

import pygame
import numpy as np
import torch
import sys
from models import PolicyNet, DEVICE
from my_2048_env import Game2048Env, move

# ========================
# Pygame Configuration
# ========================
pygame.init()
BOARD_SIZE  = 4
TILE_SIZE   = 110
MARGIN      = 12
HEADER_H    = 90
BOARD_PX    = BOARD_SIZE * TILE_SIZE + (BOARD_SIZE + 1) * MARGIN
WIN_W       = BOARD_PX + 20
WIN_H       = BOARD_PX + HEADER_H + 20

screen = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("2048 PPO Agent")

FONT       = pygame.font.SysFont("arial", 32, bold=True)
SMALL_FONT = pygame.font.SysFont("arial", 20)
TINY_FONT  = pygame.font.SysFont("arial", 15)

BG_COLOR   = (250, 248, 239)
GRID_COLOR = (187, 173, 160)
TEXT_DARK  = (119, 110, 101)
TEXT_LIGHT = (249, 246, 242)

TILE_COLORS = {
    0:    (205, 193, 180),
    2:    (238, 228, 218),
    4:    (237, 224, 200),
    8:    (242, 177, 121),
    16:   (245, 149, 99),
    32:   (246, 124, 95),
    64:   (246, 94, 59),
    128:  (237, 207, 114),
    256:  (237, 204, 97),
    512:  (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (60,  200, 100),
    8192: (30,  160, 80),
}

# ========================
# Drawing
# ========================
def draw_board(board, score, max_tile, moves, legal_count, game_over=False, paused=False):
    screen.fill(BG_COLOR)

    # Header
    title = FONT.render("2048 — PPO Agent", True, TEXT_DARK)
    screen.blit(title, (10, 8))

    score_text = SMALL_FONT.render(f"Score: {int(score):,}", True, TEXT_DARK)
    screen.blit(score_text, (10, 48))

    info_text = TINY_FONT.render(
        f"Max: {max_tile}  |  Moves: {moves}  |  Legal: {legal_count}"
        + ("  |  PAUSED (P)" if paused else "")
        + ("  |  GAME OVER — SPACE to restart" if game_over else ""),
        True, (255, 60, 60) if game_over else TEXT_DARK
    )
    screen.blit(info_text, (10, 70))

    # Grid
    x0 = 10
    y0 = HEADER_H

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            value = int(board[i, j])
            color = TILE_COLORS.get(value, TILE_COLORS[8192])

            x = x0 + MARGIN + j * (TILE_SIZE + MARGIN)
            y = y0 + MARGIN + i * (TILE_SIZE + MARGIN)

            pygame.draw.rect(screen, color, [x, y, TILE_SIZE, TILE_SIZE], border_radius=6)

            if value != 0:
                text_color = TEXT_LIGHT if value > 4 else TEXT_DARK
                fs = 48 if value < 100 else (36 if value < 1000 else (28 if value < 10000 else 22))
                f  = pygame.font.SysFont("arial", fs, bold=True)
                txt = f.render(str(value), True, text_color)
                tr  = txt.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                screen.blit(txt, tr)

    pygame.display.flip()

# ========================
# Legal moves helper
# ========================
def get_legal_actions(board):
    return [a for a in range(4) if not np.array_equal(board, move(board, a))]

# ========================
# Model loading
# ========================
def load_ppo_model(path="ppo_policy_2.pth"):
    model = PolicyNet().to(DEVICE)
    ckpt  = torch.load(path, map_location=DEVICE, weights_only=False)
    if isinstance(ckpt, dict) and "policy" in ckpt:
        model.load_state_dict(ckpt["policy"])
        print(f"✓ Loaded PPO policy from '{path}' "
              f"(ep={ckpt.get('episodes','?')} best={ckpt.get('highest_tile','?')})")
    else:
        model.load_state_dict(ckpt)
        print(f"✓ Loaded PPO weights from '{path}'")
    model.eval()
    return model

# ========================
# Main
# ========================
def evaluate(model_path="ppo_policy_2.pth", delay_ms=80):
    env   = Game2048Env()
    model = load_ppo_model(model_path)

    board, _ = env.reset()
    game_over   = False
    total_score = 0.0
    moves       = 0
    paused      = False

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_SPACE:
                    board, _ = env.reset()
                    game_over   = False
                    total_score = 0.0
                    moves       = 0

                elif event.key == pygame.K_p:
                    paused = not paused

                elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    delay_ms = max(0, delay_ms - 20)

                elif event.key == pygame.K_MINUS:
                    delay_ms += 20

        legal_actions = get_legal_actions(board)
        max_tile      = int(board.max())

        draw_board(board, total_score, max_tile, moves,
                   len(legal_actions), game_over, paused)

        if not game_over and not paused:
            if not legal_actions:
                game_over = True
                print(f"Game over | Score: {int(total_score):,} | Max tile: {max_tile} | Moves: {moves}")
                continue

            state = torch.FloatTensor(board.flatten().astype(np.float32)).unsqueeze(0).to(DEVICE)

            with torch.no_grad():
                probs = model(state).cpu().numpy()[0]

            # Mask illegal actions and pick greedily
            masked = np.full(4, -np.inf)
            for a in legal_actions:
                masked[a] = probs[a]
            action = int(np.argmax(masked))

            board, reward, done, _, info = env.step(action)
            total_score += reward
            moves += 1

            if done:
                game_over = True
                print(f"Game over | Score: {int(total_score):,} | Max tile: {int(board.max())} | Moves: {moves}")

            if delay_ms > 0:
                pygame.time.delay(delay_ms)

        clock.tick(60)

    pygame.quit()


# ========================
# Entry point
# ========================
if __name__ == "__main__":
    path = "ppo_policy_2.pth"
    if len(sys.argv) > 1:
        path = sys.argv[1]

    # Check for best model
    import os
    best = "ppo_policy_best.pth"
    if os.path.exists(best) and path == "ppo_policy_2.pth":
        print(f"Found best-model checkpoint '{best}' — using it instead.")
        path = best

    evaluate(model_path=path)
