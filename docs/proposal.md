---
layout: default
title: Proposal
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

  :root {
    --bg: #0a0a0a;
    --surface: #111111;
    --border: #1f1f1f;
    --accent: #e8c547;
    --accent2: #e87d47;
    --text: #e8e8e0;
    --muted: #666660;
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
    content: 'Proposal';
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
    font-size: 11px;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .breadcrumb a {
    color: var(--muted);
    text-decoration: none;
    transition: color 0.2s;
  }

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
    font-size: 16px;
    color: var(--muted);
    max-width: 520px;
    line-height: 1.7;
    margin: 0;
  }

  /* ── Content ── */
  .content-wrap {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 60px 100px;
  }

  /* ── Section ── */
  .section {
    padding: 72px 0;
    border-bottom: 1px solid var(--border);
    display: grid;
    grid-template-columns: 260px 1fr;
    gap: 60px;
    align-items: start;
  }

  .section:last-child {
    border-bottom: none;
  }

  .section-meta {
    padding-top: 6px;
  }

  .section-num {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.25em;
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
    font-size: 22px;
    font-weight: 800;
    letter-spacing: -0.01em;
    line-height: 1.2;
    margin: 0;
    color: var(--text);
  }

  .section-body {
    font-size: 15px;
    line-height: 1.85;
    color: #4a4a44;
  }

  .section-body p {
    margin: 0 0 20px 0;
  }

  .section-body p:last-child {
    margin-bottom: 0;
  }

  .section-body strong {
    color: var(--text);
    font-weight: 700;
  }

  /* ── Goals Cards ── */
  .goals-grid {
    display: flex;
    flex-direction: column;
    gap: 1px;
    background: var(--border);
  }

  .goal-card {
    background: var(--surface);
    padding: 32px 36px;
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 24px;
    align-items: start;
  }

  .goal-tier {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .goal-badge {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 4px 10px;
    border: 1px solid;
    width: fit-content;
  }

  .goal-badge.minimum  { color: var(--muted);  border-color: var(--muted); }
  .goal-badge.realistic{ color: var(--accent);  border-color: var(--accent); }
  .goal-badge.moonshot { color: var(--accent2); border-color: var(--accent2); }

  .goal-tile {
    font-family: 'Space Mono', monospace;
    font-size: 28px;
    font-weight: 700;
    color: var(--text);
    line-height: 1;
    margin-top: 8px;
  }

  .goal-tile.minimum  { color: var(--muted); }
  .goal-tile.realistic{ color: var(--accent); }
  .goal-tile.moonshot { color: var(--accent2); }

  .goal-desc {
    font-size: 14px;
    line-height: 1.75;
    color: #4a4a44;
    padding-top: 4px;
  }

  /* ── Eval metrics ── */
  .metrics-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1px;
    background: var(--border);
    margin-bottom: 24px;
  }

  .metric-card {
    background: var(--surface);
    padding: 28px 32px;
  }

  .metric-card h4 {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent);
    margin: 0 0 10px 0;
  }

  .metric-card p {
    font-size: 14px;
    line-height: 1.7;
    color: #4a4a44;
    margin: 0;
  }

  /* ── AI tools tag ── */
  .ai-tag {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    border: 1px solid var(--border);
    padding: 14px 20px;
    font-size: 14px;
    color: var(--muted);
    margin-top: 4px;
  }

  .ai-tag::before {
    content: '⌥';
    color: var(--accent);
    font-size: 16px;
  }

  /* ── Nav footer ── */
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
    font-size: 11px;
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
    .metrics-grid { grid-template-columns: 1fr; }
    .goal-card { grid-template-columns: 1fr; }
    .doc-nav { padding: 32px 24px; }
    .page-header::before { display: none; }
  }
</style>

<div class="page-header">
  <div class="breadcrumb">
    <a href="index.html">Home</a>
    /
    <span>Proposal</span>
  </div>
  <h1>Project Proposal</h1>
  <p>Defining the scope, goals, and evaluation strategy for training a reinforcement learning agent to master 2048.</p>
</div>

<div class="content-wrap">

  <!-- Summary -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">01</div>
      <h2 class="section-title">Summary</h2>
    </div>
    <div class="section-body">
      <p>
        2048 is a game about coalescing powers of 2 — moving tiles up, right, left, and down — into higher powers of 2, with the goal of reaching 2048 in a single game. It relies on <strong>careful space management</strong>, as newly generated blocks can appear on any free cell and cannot immediately merge, and <strong>delayed rewards</strong>, requiring the agent to build up multi-step sequences to reach an optimal board state.
      </p>
      <p>
        The agent takes as input the current state of the board along with previous moves, and outputs the next action — aiming to converge on the 2048 tile through learned policy.
      </p>
    </div>
  </div>

  <!-- Goals -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">02</div>
      <h2 class="section-title">Project Goals</h2>
    </div>
    <div class="goals-grid">
      <div class="goal-card">
        <div class="goal-tier">
          <span class="goal-badge minimum">Minimum</span>
          <span class="goal-tile minimum">512</span>
        </div>
        <p class="goal-desc">
          Implement a basic RL agent with Q-learning or DQN that plays 2048 logically until it can reach a 512 tile, or performs measurably better than random moves.
        </p>
      </div>
      <div class="goal-card">
        <div class="goal-tier">
          <span class="goal-badge realistic">Realistic</span>
          <span class="goal-tile realistic">1024</span>
        </div>
        <p class="goal-desc">
          Compare different RL algorithms against each other — testing varying reward thresholds and strategies — to evaluate performance differences and examine learning curves over time.
        </p>
      </div>
      <div class="goal-card">
        <div class="goal-tier">
          <span class="goal-badge moonshot">Moonshot</span>
          <span class="goal-tile moonshot">2048</span>
        </div>
        <p class="goal-desc">
          Focus on a single RL algorithm until reaching the 2048 tile somewhat consistently, or extend performance to n×n board configurations.
        </p>
      </div>
    </div>
  </div>

  <!-- Algorithms -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">03</div>
      <h2 class="section-title">AI / ML Algorithms</h2>
    </div>
    <div class="section-body">
      <p>
        The primary approach uses <strong>model-free, off-policy methods</strong> — specifically Q-learning and Deep Q-Networks (DQN). These are well-suited to 2048's structure: a discrete action space, clear state representation as a 4×4 grid, and rewards tied to tile merges.
      </p>
      <p>
        If time allows, the project may explore <strong>interactive reinforcement learning</strong> — benchmarking the agent against varying human skill levels as an additional evaluation axis.
      </p>
    </div>
  </div>

  <!-- Evaluation -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">04</div>
      <h2 class="section-title">Evaluation Plan</h2>
    </div>
    <div class="section-body">
      <div class="metrics-grid">
        <div class="metric-card">
          <h4>Quantitative</h4>
          <p>Track highest tile reached and average score across training runs. Compare against a random-move baseline and a greedy tile-merging heuristic.</p>
        </div>
        <div class="metric-card">
          <h4>Qualitative</h4>
          <p>Examine emergent strategies: corner anchoring, edge consolidation, multi-step merge planning. Visualize board state over time and Q-value heatmaps.</p>
        </div>
      </div>
      <p>
        Visualizations will include board state playback over game episodes and <strong>Q-value heatmaps</strong> showing which reward signals the agent prioritizes, making the learned strategy interpretable and comparable across algorithms.
      </p>
    </div>
  </div>

  <!-- AI Tool Usage -->
  <div class="section">
    <div class="section-meta">
      <div class="section-num">05</div>
      <h2 class="section-title">AI Tool Usage</h2>
    </div>
    <div class="section-body">
      <p>AI tooling was used to assist with installation and setup of training environments.</p>
      <div class="ai-tag">AI assisted with environment installation and configuration</div>
    </div>
  </div>

</div>

<div class="doc-nav">
  <a href="index.html">← Home</a>
  <span class="doc-nav-center">PowerOf2 · CS 175</span>
  <a href="status.html">Status Report →</a>
</div>
