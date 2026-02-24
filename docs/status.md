---
layout: default
title: Status
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

  :root {
    --bg: #f5f4ef;
    --surface: #eceae2;
    --border: #d8d5c8;
    --accent: #b8860b;
    --accent2: #c4521a;
    --accent3: #1a6fa8;
    --text: #1a1a16;
    --muted: #7a7a72;
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    margin: 0;
    padding: 0;
  }

  /* ── Page Header ── */
  .page-header {
    padding: 80px 60px 60px;
    border-bottom: 1px solid var(--border);
    position: relative;
    overflow: hidden;
  }

  .page-header::before {
    content: 'Status';
    position: absolute;
    right: -10px;
    top: 50%;
    transform: translateY(-50%);
    font-family: 'Space Mono', monospace;
    font-size: clamp(80px, 12vw, 180px);
    font-weight: 700;
    color: transparent;
    -webkit-text-stroke: 1px #c8c5b8;
    pointer-events: none;
    user-select: none;
    line-height: 1;
    white-space: nowrap;
  }

  .breadcrumb {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .breadcrumb a { color: var(--muted); text-decoration: none; transition: color 0.2s; }
  .breadcrumb a:hover { color: var(--accent); }
  .breadcrumb span { color: var(--accent); }

  .page-header h1 {
    font-size: clamp(36px, 5vw, 64px);
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 0 0 16px 0;
    line-height: 1.05;
  }

  .page-header p {
    font-size: 18px;
    color: var(--muted);
    max-width: 560px;
    line-height: 1.7;
    margin: 0;
  }

  /* ── Layout ── */
  .content-wrap {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 60px 100px;
  }

  .section {
    padding: 72px 0;
    border-bottom: 1px solid var(--border);
    display: grid;
    grid-template-columns: 260px 1fr;
    gap: 60px;
    align-items: start;
  }

  .section:last-child { border-bottom: none; }

  .section-meta { padding-top: 6px; }

  .section-num {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .section-num::before {
    content: '';
    display: inline-block;
    width: 20px;
    height: 1px;
    background: var(--accent);
  }

  .section-title {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: -0.01em;
    line-height: 1.2;
    margin: 0;
    color: var(--text);
  }

  .section-body {
    font-size: 17px;
    line-height: 1.9;
    color: #4a4a44;
  }

  .section-body p { margin: 0 0 20px 0; }
  .section-body p:last-child { margin-bottom: 0; }
  .section-body strong { color: var(--text); font-weight: 700; }

  /* ── Sub-heading ── */
  .sub-heading {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent);
    margin: 32px 0 16px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .sub-heading::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }

  /* ── Key design choices ── */
  .design-grid {
    display: flex;
    flex-direction: column;
    gap: 1px;
    background: var(--border);
    margin-bottom: 32px;
  }

  .design-card {
    background: var(--surface);
    padding: 24px 28px;
    display: grid;
    grid-template-columns: 28px 1fr;
    gap: 16px;
    align-items: start;
  }

  .design-icon {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: var(--accent);
    padding-top: 3px;
  }

  .design-content {}

  .design-title {
    font-size: 16px;
    font-weight: 700;
    color: var(--text);
    margin: 0 0 6px 0;
    line-height: 1.3;
  }

  .design-desc {
    font-size: 15px;
    color: var(--muted);
    line-height: 1.75;
    margin: 0;
  }

  /* ── Math formula block ── */
  .formula-block {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    padding: 20px 24px;
    margin: 20px 0;
    font-family: 'Space Mono', monospace;
    font-size: 15px;
    color: var(--text);
    overflow-x: auto;
  }

  /* ── DQN hyperparams ── */
  .hyperparam-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1px;
    background: var(--border);
    margin: 20px 0;
  }

  .hyperparam-item {
    background: var(--surface);
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
  }

  .hyperparam-key {
    font-family: 'Space Mono', monospace;
    font-size: 14px;
    color: var(--muted);
  }

  .hyperparam-val {
    font-family: 'Space Mono', monospace;
    font-size: 15px;
    font-weight: 700;
    color: var(--accent);
  }

  /* ── Bug / fix cards ── */
  .bug-list {
    display: flex;
    flex-direction: column;
    gap: 1px;
    background: var(--border);
    margin-bottom: 24px;
  }

  .bug-card {
    background: var(--surface);
    padding: 28px 32px;
  }

  .bug-header {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 14px;
  }

  .bug-tag {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 4px 10px;
    border: 1px solid;
    white-space: nowrap;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .bug-tag.issue  { color: var(--accent2); border-color: var(--accent2); }
  .bug-tag.fix    { color: #5ec47a;        border-color: #5ec47a; }

  .bug-title {
    font-size: 17px;
    font-weight: 700;
    color: var(--text);
    line-height: 1.4;
  }

  .bug-body {
    font-size: 15px;
    color: var(--muted);
    line-height: 1.8;
  }

  .bug-fix {
    margin-top: 14px;
    padding-top: 14px;
    border-top: 1px solid var(--border);
    display: flex;
    gap: 14px;
    align-items: flex-start;
  }

  .bug-fix p {
    font-size: 13px;
    color: #4a4a44;
    line-height: 1.7;
    margin: 0;
  }

  /* ── Evaluation image ── */
  .eval-img-wrap {
    position: relative;
    margin: 24px 0;
    display: inline-block;
    width: 100%;
  }

  .eval-img-wrap::before {
    content: '';
    position: absolute;
    inset: -1px;
    border: 1px solid var(--border);
    pointer-events: none;
    z-index: 1;
  }

  .eval-img-wrap::after {
    content: 'Score: 4,456 — Max tile: 512';
    position: absolute;
    bottom: 16px;
    left: 16px;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent);
    background: rgba(245,244,239,0.92);
    padding: 6px 10px;
    z-index: 2;
  }

  .eval-img-wrap.no-caption::after {
    display: none;
  }

  .eval-img-wrap img {
    display: block;
    width: 100%;
    max-width: 420px;
    height: auto;
  }

  /* ── Stat row ── */
  .stat-row {
    display: flex;
    gap: 40px;
    margin: 24px 0;
    flex-wrap: wrap;
  }

  .stat { display: flex; flex-direction: column; gap: 4px; }

  .stat-value {
    font-family: 'Space Mono', monospace;
    font-size: 28px;
    font-weight: 700;
    color: var(--accent);
    line-height: 1;
  }

  .stat-label {
    font-size: 13px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* ── Remaining goals ── */
  .goals-list {
    display: flex;
    flex-direction: column;
    gap: 1px;
    background: var(--border);
  }

  .goal-item {
    background: var(--surface);
    padding: 20px 28px;
    display: flex;
    align-items: center;
    gap: 16px;
    font-size: 16px;
    color: #4a4a44;
    line-height: 1.6;
  }

  .goal-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--accent);
    flex-shrink: 0;
  }

  .goal-dot.pending { background: var(--muted); }

  /* ── Resources ── */
  .refs-list {
    display: flex;
    flex-direction: column;
    gap: 0;
    border-top: 1px solid var(--border);
  }

  .ref-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 0;
    border-bottom: 1px solid var(--border);
    text-decoration: none;
    color: var(--muted);
    font-size: 16px;
    transition: color 0.2s;
    gap: 20px;
  }

  .ref-item:hover { color: var(--text); }
  .ref-item:hover .ref-arrow { color: var(--accent); transform: translate(4px, -4px); }

  .ref-name { font-weight: 600; color: var(--text); font-size: 14px; min-width: 220px; }
  .ref-url { font-family: 'Space Mono', monospace; font-size: 11px; color: var(--muted); flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .ref-arrow { font-size: 14px; transition: transform 0.2s, color 0.2s; flex-shrink: 0; }

  /* ── AI disclaimer tags ── */
  .ai-tags {
    display: flex;
    flex-direction: column;
    gap: 1px;
    background: var(--border);
  }

  .ai-tag-item {
    background: var(--surface);
    padding: 16px 24px;
    font-size: 16px;
    color: #4a4a44;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .ai-tag-item::before {
    content: '⌥';
    color: var(--accent);
    font-size: 14px;
    flex-shrink: 0;
  }

  /* ── Video link ── */
  .video-link {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    border: 1px solid var(--border);
    padding: 16px 24px;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
    text-decoration: none;
    transition: border-color 0.2s, color 0.2s;
    margin-top: 8px;
  }

  .video-link:hover { border-color: var(--accent); color: var(--accent); }

  /* ── Doc nav ── */
  .doc-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 40px 60px;
    border-top: 1px solid var(--border);
    flex-wrap: wrap;
    gap: 16px;
  }

  .doc-nav a {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: color 0.2s;
  }

  .doc-nav a:hover { color: var(--accent); }

  .doc-nav-center {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #aaa9a0;
  }

  @media (max-width: 768px) {
    .page-header, .content-wrap { padding-left: 24px; padding-right: 24px; }
    .section { grid-template-columns: 1fr; gap: 24px; }
    .hyperparam-grid { grid-template-columns: 1fr; }
    .doc-nav { padding: 32px 24px; }
    .page-header::before { display: none; }
  }
</style>

<div class="page-header">
  <div class="breadcrumb">
    <a href="index.html">Home</a>
    /
    <span>Status Report</span>
  </div>
  <h1>Status Report</h1>
  <p>A mid-project update covering our approach, key design decisions, issues encountered, and what remains ahead.</p>
</div>

<div class="content-wrap">

  <!-- Summary -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">01</div>
      <h2 class="section-title">Project Summary</h2>
    </div>
    <div class="section-body">
      <p>
        In this project, we train two different models using two different approaches and compare their performance on the game 2048. Specifically, we implement and evaluate <strong>PPO (Proximal Policy Optimization)</strong> and <strong>DQN (Deep Q-Network)</strong>, then compare which model advances further — measured by highest tile reached and total score — as well as examining the strengths and weaknesses each approach exhibits in the context of 2048's state space.
      </p>
    </div>
  </div>

  <!-- DQN Approach -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">02</div>
      <h2 class="section-title">Approach — DQN</h2>
    </div>
    <div class="section-body">
      <p>
        One of the models we are training is a <strong>Deep Q-Network (DQN)</strong> using a Multilayer Perceptron policy. DQN takes in a 4×4 2D array representing the board state, where <strong>0 represents empty cells</strong> and positive integers represent the power of 2 occupying that cell — for example, a cell with value 3 represents 2³ = 8. This encoded array is passed to a hidden MLP network that learns patterns correlated with high rewards, then outputs a discrete action (0–3, corresponding to up, down, left, right) based on the estimated Q-value for each action.
      </p>
      <p>
        After making the selected move, the transition is stored in a <strong>replay buffer</strong>. During training, DQN samples randomly from this buffer and checks the resulting board state, receiving rewards for transitions that lead to a higher total score. This decouples the temporal order of experience from learning, reducing correlation between consecutive updates.
      </p>

      <div class="sub-heading">Loss Function</div>
      <div class="formula-block">
        L(θ) = E[(y − Q(s, a; θ))²]<br><br>
        where y = r + γ · max_a' Q(s', a'; θ⁻)
      </div>
      <p>
        The target Q-value <strong>y</strong> is computed using a separate frozen target network (θ⁻), updated periodically. This stabilizes training by preventing the moving target problem inherent in naive Q-learning, where the network would otherwise be chasing a constantly shifting objective. Gradients are backpropagated through the loss to update the online network θ.
      </p>

      <div class="sub-heading">Hyperparameters</div>
      <div class="hyperparam-grid">
        <div class="hyperparam-item"><span class="hyperparam-key">learning_rate</span><span class="hyperparam-val">1e-2</span></div>
        <div class="hyperparam-item"><span class="hyperparam-key">buffer_size</span><span class="hyperparam-val">5,000</span></div>
        <div class="hyperparam-item"><span class="hyperparam-key">learning_starts</span><span class="hyperparam-val">100</span></div>
        <div class="hyperparam-item"><span class="hyperparam-key">batch_size</span><span class="hyperparam-val">32</span></div>
        <div class="hyperparam-item"><span class="hyperparam-key">exploration_fraction</span><span class="hyperparam-val">0.1</span></div>
        <div class="hyperparam-item"><span class="hyperparam-key">total_timesteps</span><span class="hyperparam-val">5,000</span></div>
      </div>

      <div class="sub-heading">Training Curve</div>
      <div class="eval-img-wrap no-caption" style="margin-bottom: 28px;">
        <img src="DQNTraining.png" alt="DQN training curve" />
      </div>

      <p>
        With the default DQN environment, the model does not learn to avoid illegal moves — moves where the board state does not change — and ultimately gets stuck repeating them indefinitely. Penalizing illegal moves was attempted, but the model still lacked persistent memory of <em>why</em> a specific move was illegal for a given board state, causing it to repeat the same mistake. The next step is to mask illegal moves entirely at the action selection stage, preventing them from ever being chosen.
      </p>

      <div class="sub-heading">Failure Mode</div>
      <div class="eval-img-wrap no-caption">
        <img src="DQNFail.png" alt="DQN stuck on illegal moves" />
      </div>
    </div>
  </div>

  <!-- PPO Approach -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">03</div>
      <h2 class="section-title">Approach — PPO</h2>
    </div>
    <div class="section-body">
      <p>
        The PPO model uses a custom-built environment and training loop with a <strong>CNN + MLP dual-path architecture</strong>. The policy network takes the 4×4 board as input — log2-encoded and passed through both a convolutional spatial path and a flattened MLP path — then outputs a probability distribution over the four possible moves.
      </p>
      <div class="sub-heading">Algorithm Overview</div>

<p>
  The agent is trained using <strong>Proximal Policy Optimization (PPO)</strong>, a policy-gradient reinforcement learning algorithm designed to provide stable and sample-efficient updates. PPO operates by repeatedly collecting trajectories of interaction data from the environment, storing them in a rollout buffer, and then performing multiple epochs of minibatch optimization over that fixed dataset. Each interaction step produces a tuple \( (s_t, a_t, r_t, s_{t+1}) \), where the state \( s_t \) corresponds to the log₂-encoded 4×4 board, the action \( a_t \) is one of four discrete moves, and the reward \( r_t \) comes from merge scores and shaping bonuses.
</p>

<p>
  The policy network outputs a probability distribution \( \pi_\theta(a \mid s) \), while a separate value network estimates \( V_\phi(s) \). PPO improves the policy by maximizing a clipped surrogate objective that prevents destructive policy updates:
</p>

<div class="formula-block">
  \( L^{\text{PPO}}(\theta) =
  \mathbb{E}_t \Big[
    \min \Big(
      r_t(\theta)\hat{A}_t,\;
      \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t
    \Big)
  \Big] \)
</div>

<p>where</p>

<div class="formula-block">
  \( r_t(\theta) =
  \frac{\pi_\theta(a_t \mid s_t)}
       {\pi_{\theta_{\text{old}}}(a_t \mid s_t)} \)
</div>

<p>
  and \( \hat{A}_t \) is the advantage estimate. The clipping term limits how far the policy can move during each update, preventing large shifts that could collapse previously learned behavior.
</p>

<p>
  The value function is trained using a regression objective:
</p>

<div class="formula-block">
  \( L^{\text{value}}(\phi) =
  \mathbb{E}_t \Big[
    (V_\phi(s_t) - \hat{R}_t)^2
  \Big] \)
</div>

<p>
  where \( \hat{R}_t \) represents the bootstrapped return. An entropy bonus is added to encourage exploration:
</p>

<div class="formula-block">
  \( L^{\text{entropy}}(\theta) =
  \mathbb{E}_t \big[
    \mathcal{H}(\pi_\theta(\cdot \mid s_t))
  \big] \)
</div>

<p>
  The final optimization objective combines these components:
</p>

<div class="formula-block">
  \( L =
  L^{\text{PPO}}
  - c_1 L^{\text{value}}
  + c_2 L^{\text{entropy}} \)
</div>

<p>
  Advantage estimation uses <strong>Generalized Advantage Estimation (GAE)</strong>, which balances bias and variance:
</p>

<div class="formula-block">
  \( \hat{A}_t =
  \sum_{l=0}^{\infty}
  (\gamma \lambda)^l \delta_{t+l} \)
  <br><br>
  \( \delta_t =
  r_t + \gamma V(s_{t+1}) - V(s_t) \)
</div>

<p>
  This produces smoother gradients and more stable learning compared to single-step or Monte Carlo returns.
</p>

<p>
  In the case of 2048, the observation space is a deterministic 4×4 grid whose tile magnitudes vary exponentially. Direct numerical input would create poorly scaled features, so the board is log₂-encoded, compressing tile values into a compact range. The encoded board is processed by a dual-path architecture: a CNN branch captures spatial structure (adjacency, merge opportunities, monotonic gradients), while a parallel MLP branch models global board statistics. These feature streams are concatenated and mapped to a four-action categorical distribution.
</p>

<p>
  The reward function uses \( r = \log_2(\text{merge\_score} + 1) \), stabilizing gradient variance, and is augmented with shaping bonuses encouraging corner anchoring, monotonicity, and maintaining empty cells. These shaping signals accelerate learning by providing dense feedback without altering the optimal policy.
</p>

<p>
  Training proceeds using large rollout batches (4096 steps per update), ensuring gradient estimates reflect diverse board configurations. The buffer is shuffled into minibatches and optimized over multiple epochs to improve sample efficiency. Separate Adam optimizers are used for policy and value networks, while a cosine annealing schedule gradually reduces step sizes. Gradient clipping (norm ≤ 0.5) prevents rare high-reward transitions from destabilizing updates.
</p>

<p>
  A reproducible configuration specifies parameters such as discount factor \( \gamma \) (typically 0.99), GAE parameter \( \lambda \) (often 0.95), PPO clipping coefficient \( \epsilon \) (commonly 0.1–0.2), minibatch size, optimization epochs, entropy coefficient, and value loss weight. These defaults follow established PPO literature (Schulman et al., 2016; 2017).
</p>
      <div class="sub-heading">Key Design Choices</div>
      <div class="design-grid">

        <div class="design-card">
          <span class="design-icon">01</span>
          <div class="design-content">
            <p class="design-title">Log2-Encoded Board → CNN + MLP Dual-Path Network</p>
            <p class="design-desc">Raw tile values span five orders of magnitude (2–131072), making them poor direct inputs. Log2 encoding compresses this to a uniform 1–17 range, giving spatial convolutions and the flat MLP path equally scaled features to work with.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">02</span>
          <div class="design-content">
            <p class="design-title">Reward = log₂(merge_score + 1)</p>
            <p class="design-desc">Using raw merge scores as reward creates extremely high-variance signal — merging a 1024 tile gives 500× more reward than merging a 2 tile. Log2 transformation keeps the signal bounded and consistent across all tile magnitudes.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">03</span>
          <div class="design-content">
            <p class="design-title">Corner Placement Bonus</p>
            <p class="design-desc">The agent receives a bonus when the maximum tile occupies a corner. Corner anchoring is a core human strategy: it enables cascading collapses where a sequence of moves merges multiple descending tiles in one sweep without displacing the highest tile.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">04</span>
          <div class="design-content">
            <p class="design-title">Monotonicity Bonus</p>
            <p class="design-desc">Rewards moves that produce consistently increasing or decreasing tile values across rows and columns. Monotonic arrangements make multi-tile merges possible in a single move, dramatically compressing the board and freeing space for future tiles.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">05</span>
          <div class="design-content">
            <p class="design-title">Empty Cell Bonus</p>
            <p class="design-desc">A small bonus per empty cell encourages the agent to keep the board open. Fewer empty cells means fewer future moves are legal, accelerating game-over states. This bonus discourages the agent from filling the board prematurely.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">06</span>
          <div class="design-content">
            <p class="design-title">Generalized Advantage Estimation (GAE)</p>
            <p class="design-desc">GAE reduces variance in policy gradient updates by blending multi-step return estimates. Rather than using a single-step TD error or a full Monte Carlo return, GAE interpolates between them (via λ) to balance the tradeoff between bias and variance when estimating how good a specific action was relative to average policy behavior.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">07</span>
          <div class="design-content">
            <p class="design-title">Large Rollout Buffer (4096 steps)</p>
            <p class="design-desc">Collecting 4096 environment steps before each update ensures the policy gradient estimate is computed over a diverse batch of board states and action outcomes, reducing the influence of any single lucky or unlucky episode.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">08</span>
          <div class="design-content">
            <p class="design-title">Mini-Batch PPO Updates</p>
            <p class="design-desc">The rollout buffer is split into mini-batches for multiple epochs of gradient updates. The PPO clipping objective limits how much the policy can shift from its previous version per update, preventing destructive overshooting while still making meaningful progress each iteration.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">09</span>
          <div class="design-content">
            <p class="design-title">Separate Adam Optimizers + Cosine LR Schedule</p>
            <p class="design-desc">Policy and value networks use independent Adam optimizers with different learning rates, allowing each to converge at its natural pace. A cosine annealing schedule with warm restarts reduces the learning rate over time, enabling fine-grained refinement after broad early exploration.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">10</span>
          <div class="design-content">
            <p class="design-title">Gradient Clipping at 0.5</p>
            <p class="design-desc">Gradient clipping prevents exploding gradients — cases where a single large update destabilizes previously learned weights. Without clipping, rare high-reward merges can produce gradient spikes that cause the policy to catastrophically forget strategies it had already learned.</p>
          </div>
        </div>

        <div class="design-card">
          <span class="design-icon">11</span>
          <div class="design-content">
            <p class="design-title">Two Saved Checkpoints</p>
            <p class="design-desc">Training maintains two separate checkpoints: the <em>latest</em> model (saved every 500 episodes and on every new best tile) and the <em>best average score</em> model (saved only when the 100-episode rolling average improves by more than 1%). This separates recency from quality for evaluation and further training.</p>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- Issues & Fixes -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">04</div>
      <h2 class="section-title">Issues &amp; Fixes</h2>
    </div>
    <div class="section-body">
      <p>Several non-trivial behavioral issues emerged during training that required targeted interventions:</p>

      <div class="bug-list" style="margin-top: 24px;">

        <div class="bug-card">
          <div class="bug-header">
            <span class="bug-tag issue">Issue</span>
            <span class="bug-title">Survival Over Legality — Repeated Illegal Moves</span>
          </div>
          <p class="bug-body">
            The agent discovered it could prolong its survival by repeatedly submitting illegal moves (moves that don't change the board state) rather than making a real move that risks triggering game-over. With only one legal move remaining, it would cycle through the three illegal ones indefinitely, achieving artificially high episode lengths without any actual progress.
          </p>
          <div class="bug-fix">
            <span class="bug-tag fix">Fix</span>
            <p>The environment was modified to strictly filter actions — only moves that result in a board state change are permitted. The action selection layer now masks illegal moves before sampling, forcing the agent to always make a move that advances the game state.</p>
          </div>
        </div>

        <div class="bug-card">
          <div class="bug-header">
            <span class="bug-tag issue">Issue</span>
            <span class="bug-title">Cyclic Move Pattern — LEFT → DOWN → RIGHT → UP Loop</span>
          </div>
          <p class="bug-body">
            The agent converged on a deterministic ring pattern: LEFT, DOWN, RIGHT, UP, repeating indefinitely. This local optimum generates some merges early on but quickly fills the board without building toward high tiles, ultimately ending in game-over from a full board with no merge opportunities.
          </p>
          <div class="bug-fix">
            <span class="bug-tag fix">Fix</span>
            <p>The learning rate was increased to give the optimizer enough momentum to escape this local minimum. A higher learning rate causes larger weight updates that are sufficient to disrupt the cyclic attractor in policy space, allowing the agent to explore and discover more productive strategies.</p>
          </div>
        </div>

        <div class="bug-card">
          <div class="bug-header">
            <span class="bug-tag issue">Issue</span>
            <span class="bug-title">Descending Row Fixation — Premature Strategy Lock</span>
          </div>
          <p class="bug-body">
            The model learned to construct strictly descending rows as a strategy, which is partially correct — monotonic arrangements are good — but it locked into this pattern too rigidly. It would force descending rows even when doing so violated corner placement, ultimately preventing the highest tile from staying anchored and leading to board fragmentation.
          </p>
          <div class="bug-fix">
            <span class="bug-tag fix">Fix</span>
            <p>The architecture was upgraded from a flat MLP to a CNN + MLP dual-path network. The convolutional path processes the board spatially, allowing the model to recognize 2D positional relationships (corner anchoring, diagonal arrangements, adjacency for merging) rather than treating all 16 cells as an unordered flat vector.</p>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- Evaluation -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">05</div>
      <h2 class="section-title">Evaluation</h2>
    </div>
    <div class="section-body">
      <p>
        The two primary evaluation metrics are <strong>total score</strong> (sum of all merge values across the game, matching standard 2048 scoring) and <strong>maximum tile reached</strong>. These objectively capture both the quantity of merges and their quality.
      </p>

      <div class="stat-row">
        <div class="stat">
          <span class="stat-value">4,456</span>
          <span class="stat-label">Score (PPO)</span>
        </div>
        <div class="stat">
          <span class="stat-value">512</span>
          <span class="stat-label">Max Tile</span>
        </div>
        <div class="stat">
          <span class="stat-value">PPO</span>
          <span class="stat-label">Model</span>
        </div>
      </div>

      <div class="eval-img-wrap">
        <img src="PPO512.png" alt="PPO agent reaching 512 tile" />
      </div>

      <p>
        Qualitative evaluation will additionally examine emergent behavioral patterns: whether the model pushes high tiles to corners, whether it creates snake or diagonal formations, and how frequently it resorts to suboptimal moves under board pressure. Q-value heatmaps will be used to visualize which board states the agent values most highly.
      </p>
    </div>
  </div>

  <!-- Remaining Goals -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">06</div>
      <h2 class="section-title">Remaining Goals</h2>
    </div>
    <div class="section-body">
      <p>Work remaining before the final submission:</p>
      <div class="goals-list" style="margin-top: 20px;">
        <div class="goal-item"><span class="goal-dot pending"></span>Implement DQN illegal-move masking wrapper and rerun hyperparameter tuning</div>
        <div class="goal-item"><span class="goal-dot pending"></span>Finalize hyperparameter tuning for both PPO and DQN models</div>
        <div class="goal-item"><span class="goal-dot pending"></span>Generate learning curve visualizations (score and max tile over episodes)</div>
        <div class="goal-item"><span class="goal-dot pending"></span>Produce Q-value heatmaps for DQN to interpret reward prioritization</div>
        <div class="goal-item"><span class="goal-dot pending"></span>Run head-to-head comparison across identical evaluation episodes</div>
        <div class="goal-item"><span class="goal-dot pending"></span>Write qualitative analysis of emergent strategies per model</div>
      </div>
    </div>
  </div>

  <!-- Video -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">07</div>
      <h2 class="section-title">Video Submission</h2>
    </div>
    <div class="section-body">
      <p>A walkthrough video covering our current progress, approach, and preliminary results.</p>
      <a href="link here" class="video-link">▶ Watch Video Submission ↗</a>
    </div>
  </div>

  <!-- Resources -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">08</div>
      <h2 class="section-title">Resources Used</h2>
    </div>
    <div class="section-body">
      <div class="refs-list">
        <a href="https://github.com/Quentin18/gymnasium-2048/blob/main/README.md" class="ref-item" target="_blank">
          <span class="ref-name">2048 GitHub Repository</span>
          <span class="ref-url">github.com/Quentin18/gymnasium-2048</span>
          <span class="ref-arrow">↗</span>
        </a>
        <a href="https://stable-baselines3.readthedocs.io/en/master/modules/dqn.html" class="ref-item" target="_blank">
          <span class="ref-name">Stable Baselines3 DQN</span>
          <span class="ref-url">stable-baselines3.readthedocs.io</span>
          <span class="ref-arrow">↗</span>
        </a>
        <a href="https://arxiv.org/pdf/1312.5602" class="ref-item" target="_blank">
          <span class="ref-name">DeepMind DQN Paper</span>
          <span class="ref-url">arxiv.org/pdf/1312.5602</span>
          <span class="ref-arrow">↗</span>
        </a>
        <a href="https://arxiv.org/html/2507.05465v1" class="ref-item" target="_blank">
          <span class="ref-name">Stanford 2048 Paper</span>
          <span class="ref-url">arxiv.org/html/2507.05465v1</span>
          <span class="ref-arrow">↗</span>
        </a>
        <a href="https://medium.com/data-science/a-puzzle-for-ai-eb7a3cb8e599" class="ref-item" target="_blank">
          <span class="ref-name">Medium — A Puzzle for AI</span>
          <span class="ref-url">medium.com/data-science</span>
          <span class="ref-arrow">↗</span>
        </a>
        <a href="https://royf.org/crs/CS175/W26/CS175L2.pdf" class="ref-item" target="_blank">
          <span class="ref-name">CS175 Slides</span>
          <span class="ref-url">royf.org/crs/CS175/W26</span>
          <span class="ref-arrow">↗</span>
        </a>
      </div>
    </div>
  </div>

  <!-- AI Disclaimer -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">09</div>
      <h2 class="section-title">AI Disclaimer</h2>
    </div>
    <div class="section-body">
      <p>AI tooling was used in the following capacities:</p>
      <div class="ai-tags" style="margin-top: 16px;">
        <div class="ai-tag-item">Integrate libraries and dependencies</div>
        <div class="ai-tag-item">Create frontend design for GitHub Pages</div>
        <div class="ai-tag-item">Supplement personal learning of RL models</div>
      </div>
    </div>
  </div>

</div>

<div class="doc-nav">
  <a href="proposal.html">← Proposal</a>
  <span class="doc-nav-center">PowerOf2 · CS 175</span>
  <a href="final.html">Final Report →</a>
</div>
