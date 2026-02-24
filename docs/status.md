---
layout: default
title: Status
---

## Project Summary
In this project, we train three different models using three different approaches and compare the performance of each model on the game 2048. Specifically, we use PPO and DQN, then compare which model gets the furthest (indicated by the highest number and total score) in the game, as well as the strengths and weaknesses of each model in 2048.

## Approach
### DQN
One of the models we are training is Deep Q Learning (DQN) that uses a Multilayer Perceptron policy. This takes uses board states as input/output and makes actions (0-4, corresponding to left, right, up, and down) based on rewards (total_score). 

The loss function for DQN is $$L(\theta) = \mathbb{E}_{(s, a, r, s') \sim U(D)} \left[ \left( y - Q(s, a; \theta) \right)^2 \right]$$ where $$y = r + \gamma \max_{a'} Q(s', a'; \theta^-)$$

The base code for the 2048 game uses random moves without any learning. We used the Stable Baselines3 DQN enviromment to train a model on 2048. The hyperparameters for the MLP DQN model were:
- learning_rate=1e-2
- buffer_size =5000
- learning_starts=100
- batch_size=32
- exploration_fraction=0.1
- verbose=1
with 
- total_timesteps=5000

Unfortunately, with the default DQN environment, the model does not learn to avoid illegal moves (moves where the board state does not change) and ultimately gets stuck on said move. Because of this, the hyperparameters have not fully been tuned. To fix getting stuck, we tried to punish illegal moves, but the model still has no memory of why that move was illegal for the circumstance. Next, we will try adjusting the training protocols to avoid illegal moves altogether.

### PPO

## Evaluation

## Remaining Goals and Challenges

## Resources Used
- [2048 GitHub Repository](https://github.com/Quentin18/gymnasium-2048/blob/main/README.md)
- [Stable Baselines3 DQN](https://stable-baselines3.readthedocs.io/en/master/modules/dqn.html)
- [DeepMind Technologies DQN Paper](https://arxiv.org/pdf/1312.5602)
- [Stanford 2048 Paper](https://arxiv.org/html/2507.05465v1)
- [Medium 2048 Article](https://medium.com/data-science/a-puzzle-for-ai-eb7a3cb8e599)
- Claude/Google Gemini
