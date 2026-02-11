---
layout: default
title: Proposal
---
## Summary of the Project
2048 is a game about coalescing powers of 2, up, right, left, and down, into higher powers of 2 such that you are able to get 2048 in a single game. It relies on careful space management, due to the new block generated being able to go on any free space and being unable to coalesce at the moment, and delayed rewards, due to building up moves to reach an optimal state/score. 

Information it will take as input is the state of the board and previous moves done by the agent, as it will output the next concurrent move in the aim to make 2048.

## Project goals
Minimum goal: Implement a basic RL agent with either Q-learning/DQN that is able to play 2048 logically until it can reach a 512 tile, or performs better than random moves.

Realistic goal: Compare different RL algorithms against each other to see how performance varies, testing different reward thresholds and strategies, to evaluate how they do compared to each other, while looking at learning curves over time.

Moonshot goal: Focus on a single RL algorithm until we are able to reach the 2048 somewhat consistently, or allow performance over nxn arrays

## AI/ML algorithms
We believe that we will use model-free off-policy methods like Q-learning or DQN. If time allows we can try using interactive reinforcement learning against our skill levels in 2048.

## Evaluation Plan
To evaluate the agent, we will run different training runs while keeping track of metrics such as highest tile gotten and the average score. To compare it against a baseline naive approach, we can have a bot that plays random moves or compare it against a bot that follows a greedy heuristic for tile merging. 

To qualitatively evaluate it, we will examine the strategies that it learns and what kind of performance it has, such as keeping higher valued tiles at the edge of the board, maximizing points when merging, and planning multistep coalescing. We can visualize the games by looking at the board state over time and looking at Q-value heatmaps for the rewards to prioritize on.

## AI Tool Usage
AI was used to help with installation and setup of environments.
