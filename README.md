# Power of 2 — Reinforcement Learning & Search for 2048 Optimization

> **UC Irvine · CS 175: Project in Artificial Intelligence**  
> **Live Project Site & Walkthrough:** [leem07.github.io/PowerOf2](https://leem07.github.io/PowerOf2/)

An empirical study comparing **On-Policy Deep RL (Dual-Path PPO)**, **Off-Policy Value Learning (DQN)**, and **Heuristic-Guided Search (MCTS)** on the stochastic 2048 environment—focusing on long-horizon planning, scale-invariant reward shaping, and failure-mode diagnosis.

---

## Key Results & Model Comparison

Evaluated across 20-game standardized benchmarks measuring **2048 tile reach rate**, **average max tile**, **inference speed**, and **cross-game generalization**:

| Model Paradigm | Architecture / Search Method | 2048 Rate | Avg Max Tile | Avg Time / Game | Retains Policy Across Games? |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Dual-Path PPO** *(Best Overall)* | Custom `Conv2d` + `MLP` Actor-Critic (`23M` steps) | **10%** *(512 floor)* | **1024** | **~1.5s** | Yes (trained weights) |
| **Heuristic MCTS** | UCB Tree Search + 4 domain rollout heuristics | Reaches 2048 *(high compute)* | Compute-dependent | ~8 min *(at 2048)* | No (searches from scratch) |
| **DQN** | `stable-baselines3` MLP + Experience Replay | 0% | 64–100+ | <1s | Yes (reward plateaued) |

### Core Takeaways
* **PPO Dominates on Speed & Consistency:** Once trained (~50k episodes / 23M steps), the dual-path PPO agent plays full games in **~1.5 seconds** (under 30 seconds for a 20-game suite) with a **1024 average max tile** and a **512 minimum floor**, outperforming MCTS on 512/1024 stability at a fraction of inference latency.
* **MCTS Scales with Compute, Not Experience:** Heuristic-guided MCTS reaches 2048 when given deep rollout budgets (~8 minutes/game), but runtime is strictly hardware-bound and discards all learned knowledge after every move.
* **Reward Shaping Prevents Local-Optima Traps:** Naive raw merge scores cause reward variance across five orders of magnitude ($2$ to $2^{17}$) and induce greedy, board-fragmenting merges. Scale-invariant $\log_2$ rewards paired with corner anchoring and monotonicity penalties unlock multi-step cascading merges.

---

## Flagship Architecture: Dual-Path PPO (`CNN + MLP`)

2048 combines stochastic tile spawns ($2$ or $4$ in random empty cells), non-linear row/column collapses, and long reward horizons. Neither spatial convolutions alone nor flat MLPs alone capture the full game state—so we designed a parallel dual-path actor-critic network:

### 1. State Representation & Dual-Path Network
* **Input Encoding:** Each board cell $t$ is compressed via $\log_2(t) / 17$ into a uniform $[0, 1]$ range (with $0$ for empty cells), eliminating five orders of magnitude of raw numerical skew.
* **Spatial Path (`Conv2d`):** Processes the `(1, 4, 4)` grid (`1 → 64 → 128 → 128` channels) to capture local adjacency, diagonal traps, and corner anchoring.
* **Global Path (`MLP`):** Processes the flattened 16-cell vector (`16 → 256 → 256`) so every cell interacts globally regardless of spatial distance.
* **Policy & Value Heads:** Concatenated features (`1408 → 512 → 256`) feed separate **Actor** ($\pi_\theta(a|s) \in \mathbb{R}^4$) and **Critic** ($V_\phi(s) \in \mathbb{R}^1$) heads.

### 2. Scale-Invariant Reward Function
To align short-term feedback with long-horizon merge chains without reward hacking:

$$r_t = \log_2(\text{merge score} + 1) + 0.30 \cdot \log_2(\text{max tile} + 1) \cdot \mathbb{I}[\text{max tile in corner}] + 0.10 \cdot N_{\text{empty}} - 0.05 \cdot P_{\text{mono}}$$

* **Logarithmic Merge Base:** Merging two `512` tiles ($\log_2(1025) \approx 10$) vs. two `2` tiles ($\log_2(5) \approx 2.3$) keeps gradient magnitudes bounded across early and late game stages.
* **Corner Anchoring (`+0.30`):** Rewards keeping the highest tile stationary in a corner to enable descending snake-chain collapses.
* **Empty Cell Preservation (`+0.10/cell`):** Prevents premature board lockup and preserves branching factor against random spawns.
* **Monotonicity Penalty (`-0.05`):** Accumulates $\log_2$ differences across adjacent row/column pairs that violate monotonic ordering.

### 3. Training Configuration
* **Optimization:** Independent Adam optimizers for Actor (`lr = 1e-4`) and Critic (`lr = 5e-4`) with Cosine Annealing warm restarts ($T_0 = 2\text{M}$ steps) and gradient norm clipping (`max_norm = 0.5`).
* **Advantage Estimation:** Generalized Advantage Estimation ($\gamma = 0.997, \lambda = 0.95$) over `4,096`-step rollout buffers (`8` PPO epochs, `512` mini-batch size, $\epsilon = 0.2$ clip, `0.02` entropy bonus).
* **Checkpointing:** Dual-checkpoint saving (`latest` every 500 episodes + `best-average` triggered only when the 100-episode rolling mean improves by $>1\%$).

---

## Training Failure Modes & Engineering Fixes

Iterative debugging across baselines and early PPO runs uncovered four major failure modes—each resolved through targeted architectural or environment interventions:

| Failure Mode Observed | Root Cause | Engineering Fix |
| :--- | :--- | :--- |
| **Infinite Illegal-Move Loops** | Agent repeatedly selected directions that produced zero board change, stalling episodes indefinitely. | Added strict environment-level action masking to filter invalid moves before policy sampling. |
| **Deterministic Cyclic Loop** (`L → D → R → U`) | Early imitation/flat-MLP runs collapsed into a fixed 4-move ring attractor until board lockup. | Replaced flat MLP with the dual-path `CNN + MLP` and tuned learning rate momentum to escape local minima. |
| **Unresolved Diagonal Separation** | Flat MLP lacked spatial inductive bias to align diagonally offset mergeable tiles. | Introduced the `Conv2d` spatial branch alongside empty-cell preservation rewards. |
| **Board Fragmentation ("Holes")** | Over-weighting generic high-tile bonuses caused greedy merges that trapped isolated low-value tiles. | Lowered tile coefficient and restricted the bonus strictly to **corner-anchored** max tiles. |

---

## Baseline Approaches Explored

### Heuristic-Guided Monte Carlo Tree Search (MCTS)
* **Method:** Replaced noisy random rollouts with domain-weighted rollout evaluation combining **Empty Tile Weighting**, **Snake Monotonicity**, **Corner Bias**, and **Tile Smoothness**, balanced via UCB exploration ($c$).
* **Finding:** Reliable path to `2048` when allotted high simulation budgets (~8 min/game), confirming the validity of our domain heuristics before embedding them into PPO's reward function.

### Deep Q-Network (DQN)
* **Method:** Off-policy MLP Q-network (`stable-baselines3`, `buffer_size = 100k`, `batch_size = 512`, `lr = 1e-4`) with target network stabilization and environment wrappers for illegal-move penalties and corner rewards.
* **Finding:** Learned basic corner-anchoring behavior, but high stochasticity and delayed credit assignment caused value estimates to plateau around max tiles of `64–100+` under limited compute budgets.

---

## Resources & Acknowledgments
* **Environment & Baselines:** [`gymnasium-2048`](https://github.com/Quentin18/gymnasium-2048), [`stable-baselines3`](https://stable-baselines3.readthedocs.io/), [`2048_MCTS`](https://github.com/poomstas/2048_MCTS)
* **Literature:** DeepMind DQN (*Mnih et al.*), Stanford 2048 RL Study (`arXiv:2507.05465v1`), UC Irvine CS 175 Course Materials.
* **Full Report & Video Demo:** [leem07.github.io/PowerOf2](https://leem07.github.io/PowerOf2/)
