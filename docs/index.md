---
layout: default
title: Home
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

  .hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 80px 60px;
    overflow: hidden;
    border-bottom: 1px solid var(--border);
  }

  .hero::before {
    content: '2048';
    position: absolute;
    right: -20px;
    top: 50%;
    transform: translateY(-50%);
    font-family: 'Space Mono', monospace;
    font-size: clamp(160px, 22vw, 320px);
    font-weight: 700;
    color: transparent;
    -webkit-text-stroke: 1px #c8c5b8;
    pointer-events: none;
    user-select: none;
    line-height: 1;
  }

  .hero-tag {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .hero-tag::before {
    content: '';
    display: inline-block;
    width: 32px;
    height: 1px;
    background: var(--accent);
  }

  h1.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(40px, 6vw, 80px);
    font-weight: 800;
    line-height: 1.05;
    margin: 0 0 24px 0;
    max-width: 700px;
    letter-spacing: -0.02em;
  }

  h1.hero-title em {
    font-style: normal;
    color: var(--accent);
  }

  .hero-subtitle {
    font-size: 17px;
    color: var(--muted);
    max-width: 480px;
    line-height: 1.7;
    margin: 0 0 48px 0;
    font-weight: 400;
  }

  .hero-cta {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
  }

  .btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--accent);
    color: #0a0a0a;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 14px 28px;
    text-decoration: none;
    transition: background 0.2s, transform 0.2s;
  }

  .btn-primary:hover {
    background: #f0d060;
    transform: translateY(-2px);
  }

  .btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    border: 1px solid var(--border);
    color: var(--muted);
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 14px 28px;
    text-decoration: none;
    transition: border-color 0.2s, color 0.2s, transform 0.2s;
  }

  .btn-secondary:hover {
    border-color: var(--accent);
    color: var(--accent);
    transform: translateY(-2px);
  }

  /* ── Board Screenshot ── */
  .board-section {
    padding: 80px 60px;
    border-bottom: 1px solid var(--border);
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
  }

  .board-label {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 20px;
  }

  .board-img-wrapper {
    position: relative;
  }

  .board-img-wrapper::before {
    content: '';
    position: absolute;
    inset: -1px;
    border: 1px solid var(--border);
    pointer-events: none;
    z-index: 1;
  }

  .board-img-wrapper::after {
    content: 'PPO — 1024 reached';
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

  .board-img-wrapper img {
    display: block;
    width: 100%;
    height: auto;
  }

  .board-text h2 {
    font-size: clamp(28px, 4vw, 44px);
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 0 0 20px 0;
    line-height: 1.1;
  }

  .board-text h2 span {
    color: var(--accent2);
  }

  .board-text p {
    color: var(--muted);
    line-height: 1.75;
    font-size: 15px;
    margin: 0 0 32px 0;
  }

  .stat-row {
    display: flex;
    gap: 40px;
  }

  .stat {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

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

  /* ── Reports ── */
  .reports-section {
    padding: 80px 60px;
    border-bottom: 1px solid var(--border);
  }

  .section-header {
    display: flex;
    align-items: baseline;
    gap: 20px;
    margin-bottom: 48px;
  }

  .section-header h2 {
    font-size: clamp(24px, 3vw, 36px);
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 0;
  }

  .section-header span {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: var(--muted);
    letter-spacing: 0.2em;
    text-transform: uppercase;
  }

  .reports-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: var(--border);
  }

  .report-card {
    background: var(--surface);
    padding: 40px;
    text-decoration: none;
    color: inherit;
    transition: background 0.2s;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .report-card:hover {
    background: #161616;
  }

  .report-card:hover .report-arrow {
    transform: translate(4px, -4px);
    color: var(--accent);
  }

  .report-num {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: var(--muted);
    letter-spacing: 0.2em;
  }

  .report-title {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.01em;
    flex: 1;
  }

  .report-arrow {
    font-size: 18px;
    transition: transform 0.2s, color 0.2s;
    align-self: flex-end;
    color: var(--muted);
  }

  /* ── References ── */
  .refs-section {
    padding: 80px 60px;
  }

  .refs-list {
    display: flex;
    flex-direction: column;
    gap: 0;
    margin-top: 48px;
    border-top: 1px solid var(--border);
  }

  .ref-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 0;
    border-bottom: 1px solid var(--border);
    text-decoration: none;
    color: var(--muted);
    font-size: 16px;
    transition: color 0.2s;
    gap: 20px;
  }

  .ref-item:hover {
    color: var(--text);
  }

  .ref-item:hover .ref-arrow {
    color: var(--accent);
    transform: translate(4px, -4px);
  }

  .ref-name {
    font-weight: 600;
    color: var(--text);
    font-size: 15px;
    min-width: 220px;
  }

  .ref-url {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: var(--muted);
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .ref-arrow {
    font-size: 14px;
    transition: transform 0.2s, color 0.2s;
    flex-shrink: 0;
  }

  /* ── Source Code ── */
  .source-bar {
    margin: 0 60px 80px;
    padding: 24px 32px;
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
  }

  .source-bar-left {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .github-icon {
    font-size: 26px;
  }

  .source-label {
    font-size: 14px;
    color: var(--muted);
  }

  .source-label strong {
    color: var(--text);
    display: block;
    font-size: 15px;
  }

  .source-link {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    text-decoration: none;
    border: 1px solid var(--accent);
    padding: 10px 20px;
    transition: background 0.2s, color 0.2s;
  }

  .source-link:hover {
    background: var(--accent);
    color: #0a0a0a;
  }

  @media (max-width: 768px) {
    .hero, .board-section, .reports-section, .refs-section { padding: 60px 24px; }
    .board-section { grid-template-columns: 1fr; gap: 48px; }
    .reports-grid { grid-template-columns: 1fr; }
    .source-bar { margin: 0 24px 60px; }
    .hero::before { display: none; }
  }
</style>

<div class="hero">
  <div class="hero-tag">CS 175 · UC Irvine · AI Project</div>
  <h1 class="hero-title">The Game of <em>2048</em>,<br>Taught to Think</h1>
  <p class="hero-subtitle">
    A deep reinforcement learning experiment pitting two algorithms against each other — DQN vs PPO — to see which one masters the art of exponential tile merging.
  </p>
  <div class="hero-cta">
    <a href="final.html" class="btn-primary">↗ Read Final Report</a>
    <a href="https://github.com/leem07/PowerOf2" class="btn-secondary">⌥ View Source</a>
  </div>
</div>

<div class="board-section">
  <div class="board-img-wrapper">
    <img src="PPO1024.png" alt="PPO agent reaching 1024 tile in 2048" />
  </div>
  <div class="board-text">
    <h2>PPO reaches<br><span>tile 1024</span></h2>
    <p>
      The Proximal Policy Optimization agent navigates the 4×4 grid through trial and error, learning corner strategies and merge sequences that push tiles to their theoretical maximum.
    </p>
    <div class="stat-row">
      <div class="stat">
        <span class="stat-value">1024</span>
        <span class="stat-label">Best Tile</span>
      </div>
      <div class="stat">
        <span class="stat-value">PPO</span>
        <span class="stat-label">Algorithm</span>
      </div>
      <div class="stat">
        <span class="stat-value">2</span>
        <span class="stat-label">Models</span>
      </div>
    </div>
  </div>
</div>

<div class="reports-section">
  <div class="section-header">
    <h2>Project Reports</h2>
    <span>03 documents</span>
  </div>
  <div class="reports-grid">
    <a href="proposal.html" class="report-card">
      <span class="report-num">01</span>
      <span class="report-title">Proposal</span>
      <span class="report-arrow">↗</span>
    </a>
    <a href="status.html" class="report-card">
      <span class="report-num">02</span>
      <span class="report-title">Status</span>
      <span class="report-arrow">↗</span>
    </a>
    <a href="final.html" class="report-card">
      <span class="report-num">03</span>
      <span class="report-title">Final</span>
      <span class="report-arrow">↗</span>
    </a>
  </div>
</div>

<div class="refs-section">
  <div class="section-header">
    <h2>References</h2>
    <span>05 sources</span>
  </div>
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
  </div>
</div>

<div class="source-bar">
  <div class="source-bar-left">
    <span class="github-icon">⌥</span>
    <div class="source-label">
      <strong>PowerOf2</strong>
      Source code on GitHub
    </div>
  </div>
  <a href="https://github.com/leem07/PowerOf2" class="source-link" target="_blank">View Repository ↗</a>
</div>
