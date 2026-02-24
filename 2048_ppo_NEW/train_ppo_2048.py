"""
train_ppo_2048.py
-----------------
PPO training for 2048 — fresh start with CNN+MLP architecture.

Run fresh:   python train_ppo_2048.py
Resume:      python train_ppo_2048.py --resume

Key design choices:
  - Log2-encoded board fed to a CNN+MLP dual-path network (see models.py)
  - Reward = log2(merge_score + 1), keeping signal bounded across tile magnitudes
  - Additional shaped bonuses for corner placement and monotonicity
  - Large rollout buffer (4096 steps), mini-batch PPO updates
  - Separate Adam optimizers + cosine LR schedule for policy and value net
  - Gradient clipping at 0.5
  - Two saved checkpoints: latest (ppo_policy_2.pth) and best-avg (ppo_policy_best.pth)
"""

import os
import sys
import math
import signal
import argparse
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

from my_2048_env import Game2048Env, move
from models import PolicyNet, ValueNet, encode_board, DEVICE

# ================================================================
# Config
# ================================================================
MODEL_PATH      = "ppo_policy_2.pth"
BEST_MODEL_PATH = "ppo_policy_best.pth"

TARGET_TILE     = 2048
TARGET_STREAK   = 5

# PPO
GAMMA           = 0.997
LAMBDA          = 0.95
CLIP_EPS        = 0.2
POLICY_LR       = 1e-4
VALUE_LR        = 5e-4
PPO_EPOCHS      = 8
MINI_BATCH      = 512
ROLLOUT_STEPS   = 4096
MAX_GRAD_NORM   = 0.5
VALUE_COEF      = 0.5
ENTROPY_COEF    = 0.02

# Reward shaping weights
W_CORNER        = 0.30
W_MONO          = 0.05
W_EMPTY         = 0.10

# Logging
LOG_EVERY       = 100
SAVE_EVERY      = 500

# ================================================================
# Helpers
# ================================================================

def get_legal_actions(board):
    return [a for a in range(4) if not np.array_equal(board, move(board, a))]


def mask_and_sample(probs: np.ndarray, legal: list):
    masked = np.array([probs[a] if a in legal else 0.0 for a in range(4)], dtype=np.float64)
    s = masked.sum()
    if s < 1e-8:
        masked = np.array([1.0 / len(legal) if a in legal else 0.0 for a in range(4)])
    else:
        masked /= s
    action   = np.random.choice(4, p=masked)
    log_prob = math.log(masked[action] + 1e-8)
    return action, log_prob


def shape_reward(merge_score: float, old_board: np.ndarray, new_board: np.ndarray) -> float:
    # Base: log2 of merge score (scale-invariant)
    reward = math.log2(merge_score + 1.0)

    max_tile    = int(new_board.max())
    corners     = [(0,0),(0,3),(3,0),(3,3)]
    corner_vals = [new_board[r,c] for r,c in corners]

    # Corner bonus
    if max_tile > 0 and max_tile == max(corner_vals):
        reward += W_CORNER * math.log2(max_tile + 1)

    # Empty cell bonus
    reward += W_EMPTY * int((new_board == 0).sum())

    # Monotonicity penalty
    mono = 0.0
    for row in new_board:
        for j in range(3):
            if row[j] > 0 and row[j+1] > 0 and row[j] > row[j+1]:
                mono += math.log2(row[j]) - math.log2(row[j+1])
    for col in new_board.T:
        for i in range(3):
            if col[i] > 0 and col[i+1] > 0 and col[i] > col[i+1]:
                mono += math.log2(col[i]) - math.log2(col[i+1])
    reward -= W_MONO * mono

    return reward


def compute_gae(rewards, values, dones, next_value):
    advantages, gae = [], 0.0
    for i in reversed(range(len(rewards))):
        delta = rewards[i] + GAMMA * next_value * (1.0 - dones[i]) - values[i]
        gae   = delta + GAMMA * LAMBDA * (1.0 - dones[i]) * gae
        advantages.insert(0, gae)
        next_value = values[i]
    returns = [a + v for a, v in zip(advantages, values)]
    return advantages, returns


def ppo_update(policy, value_net, policy_opt, value_opt,
               states_t, actions_t, old_lp_t, adv_t, ret_t):
    n = states_t.shape[0]
    indices = np.arange(n)
    for _ in range(PPO_EPOCHS):
        np.random.shuffle(indices)
        for start in range(0, n, MINI_BATCH):
            idx = indices[start:start + MINI_BATCH]
            s, a, lp, adv, ret = (states_t[idx], actions_t[idx],
                                   old_lp_t[idx], adv_t[idx], ret_t[idx])

            probs   = policy(s)
            dist    = torch.distributions.Categorical(probs)
            new_lp  = dist.log_prob(a)
            entropy = dist.entropy().mean()

            ratio  = torch.exp(new_lp - lp)
            p_loss = -torch.min(
                ratio * adv,
                torch.clamp(ratio, 1 - CLIP_EPS, 1 + CLIP_EPS) * adv
            ).mean() - ENTROPY_COEF * entropy

            policy_opt.zero_grad()
            p_loss.backward()
            nn.utils.clip_grad_norm_(policy.parameters(), MAX_GRAD_NORM)
            policy_opt.step()

            v_loss = VALUE_COEF * (ret - value_net(s).squeeze()).pow(2).mean()
            value_opt.zero_grad()
            v_loss.backward()
            nn.utils.clip_grad_norm_(value_net.parameters(), MAX_GRAD_NORM)
            value_opt.step()


# ================================================================
# Setup
# ================================================================
parser = argparse.ArgumentParser()
parser.add_argument("--resume", action="store_true",
                    help="Resume from existing checkpoint")
args = parser.parse_args()

policy    = PolicyNet().to(DEVICE)
value_net = ValueNet().to(DEVICE)

policy_opt = optim.Adam(policy.parameters(),    lr=POLICY_LR, eps=1e-5)
value_opt  = optim.Adam(value_net.parameters(), lr=VALUE_LR,  eps=1e-5)

policy_sched = optim.lr_scheduler.CosineAnnealingWarmRestarts(policy_opt, T_0=2_000_000)
value_sched  = optim.lr_scheduler.CosineAnnealingWarmRestarts(value_opt,  T_0=2_000_000)

best_tile      = 0
best_avg_score = 0.0
current_streak = 0
episodes       = 0
total_steps    = 0

# ================================================================
# Load checkpoint
# ================================================================
if args.resume and os.path.exists(MODEL_PATH):
    print(f"Resuming from {MODEL_PATH} ...")
    ckpt = torch.load(MODEL_PATH, map_location=DEVICE, weights_only=False)
    if isinstance(ckpt, dict) and "policy" in ckpt:
        try:
            policy.load_state_dict(ckpt["policy"])
            value_net.load_state_dict(ckpt["value"])
            if "policy_opt" in ckpt: policy_opt.load_state_dict(ckpt["policy_opt"])
            if "value_opt"  in ckpt: value_opt.load_state_dict(ckpt["value_opt"])
            best_tile      = ckpt.get("highest_tile", 0)
            current_streak = ckpt.get("streak", 0)
            episodes       = ckpt.get("episodes", 0)
            total_steps    = ckpt.get("steps", 0)
            best_avg_score = ckpt.get("best_avg_score", 0.0)
            print(f"  Loaded | best_tile={best_tile} | ep={episodes} | steps={total_steps:,}")
        except RuntimeError as e:
            print(f"  ⚠️  Architecture mismatch — starting fresh.\n  ({e})")
    else:
        print("  Unknown checkpoint format — starting fresh.")
else:
    if not args.resume:
        print("Fresh start. Use --resume to continue from a checkpoint.")
    else:
        print(f"No checkpoint at {MODEL_PATH} — starting fresh.")

env = Game2048Env()

# ================================================================
# Ctrl-C handler
# ================================================================
def save_checkpoint(path=MODEL_PATH):
    torch.save({
        "policy":         policy.state_dict(),
        "value":          value_net.state_dict(),
        "policy_opt":     policy_opt.state_dict(),
        "value_opt":      value_opt.state_dict(),
        "highest_tile":   best_tile,
        "streak":         current_streak,
        "episodes":       episodes,
        "steps":          total_steps,
        "best_avg_score": best_avg_score,
    }, path)
    print(f"  [saved → {path}]")


def handler(sig, frame):
    print("\nStopping safely...")
    save_checkpoint()
    raise SystemExit(0)

signal.signal(signal.SIGINT, handler)

# ================================================================
# Stats
# ================================================================
WINDOW           = 100
recent_scores    = []
recent_max_tiles = []

buf_s, buf_a, buf_r, buf_d, buf_lp, buf_v = [], [], [], [], [], []

# ================================================================
# Training loop
# ================================================================
p_count = sum(p.numel() for p in policy.parameters())
v_count = sum(p.numel() for p in value_net.parameters())
print(f"\nDevice : {DEVICE}")
print(f"Target : reach tile {TARGET_TILE} for {TARGET_STREAK} episodes in a row")
print(f"Params : policy={p_count:,}  value={v_count:,}\n")

while current_streak < TARGET_STREAK:
    board, _ = env.reset()
    done          = False
    episode_score = 0.0

    while not done:
        legal = get_legal_actions(board)
        if not legal:
            break

        state = encode_board(board).unsqueeze(0).to(DEVICE)
        with torch.no_grad():
            probs = policy(state).cpu().numpy()[0]
            value = value_net(state).cpu().numpy()[0][0]

        action, log_prob = mask_and_sample(probs, legal)

        old_board = board.copy()
        board, raw_reward, done, _, _ = env.step(action)
        episode_score += raw_reward

        shaped = shape_reward(raw_reward, old_board, board)

        buf_s.append(old_board.flatten().astype(np.float32))
        buf_a.append(action)
        buf_r.append(shaped)
        buf_d.append(float(done))
        buf_lp.append(log_prob)
        buf_v.append(value)

        total_steps += 1
        policy_sched.step(total_steps)
        value_sched.step(total_steps)

        if len(buf_s) >= ROLLOUT_STEPS or (done and buf_s):
            with torch.no_grad():
                nv = 0.0 if done else value_net(
                    encode_board(board).unsqueeze(0).to(DEVICE)
                ).cpu().numpy()[0][0]

            adv, ret = compute_gae(buf_r, buf_v, buf_d, nv)

            S  = torch.FloatTensor(np.array(buf_s)).to(DEVICE)
            A  = torch.LongTensor(buf_a).to(DEVICE)
            LP = torch.FloatTensor(buf_lp).to(DEVICE)
            AD = torch.FloatTensor(adv).to(DEVICE)
            RT = torch.FloatTensor(ret).to(DEVICE)
            AD = (AD - AD.mean()) / (AD.std() + 1e-8)

            ppo_update(policy, value_net, policy_opt, value_opt, S, A, LP, AD, RT)

            buf_s.clear(); buf_a.clear(); buf_r.clear()
            buf_d.clear(); buf_lp.clear(); buf_v.clear()

    # ---- Episode end ----
    episodes += 1
    max_tile  = int(board.max())

    recent_scores.append(episode_score)
    recent_max_tiles.append(max_tile)
    if len(recent_scores) > WINDOW:
        recent_scores.pop(0)
        recent_max_tiles.pop(0)

    avg_score    = np.mean(recent_scores)
    avg_max_tile = np.mean(recent_max_tiles)

    if max_tile > best_tile:
        best_tile = max_tile
        save_checkpoint()
        print(f"🔥 New best tile: {best_tile} "
              f"(ep {episodes} | score {int(episode_score):,} | steps {total_steps:,})")

    if max_tile >= TARGET_TILE:
        current_streak += 1
        print(f"✅ Hit {TARGET_TILE}! Streak: {current_streak}/{TARGET_STREAK} "
              f"(score {int(episode_score):,})")
    else:
        if current_streak > 0:
            print(f"  Streak broken at {current_streak} (max tile {max_tile})")
        current_streak = 0

    if episodes % LOG_EVERY == 0:
        print(f"[ep {episodes:7d} | steps {total_steps:10,}] "
              f"avg_score={avg_score:8.0f}  avg_max={avg_max_tile:6.1f}  "
              f"best={best_tile}  streak={current_streak}  "
              f"lr={policy_opt.param_groups[0]['lr']:.2e}")

    if len(recent_scores) >= WINDOW and avg_score > best_avg_score * 1.01:
        best_avg_score = avg_score
        print(f"  📈 New best avg score: {avg_score:.0f}")
        save_checkpoint(BEST_MODEL_PATH)

    if episodes % SAVE_EVERY == 0:
        save_checkpoint()

# ================================================================
print(f"\n🏆 Reached {TARGET_TILE} × {TARGET_STREAK} in a row!")
save_checkpoint()
