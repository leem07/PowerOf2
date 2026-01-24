---
layout: default
title: Proposal
---
## Summary of the Project
Duckietown is a simulation driven program that navigates a duckiebot through a virtual world, though it can also be used on physical hardware. Our goal is to train our duckiebot using various RL algorithms in order to determine the best results based on the given task. Our duckiebot will be given the simulated world with these variables and be expected to not veer off course or crash into obstacles/walls.

## Project goals
Minimum goal: The duckiebot is able to follow a straight line.

Realistic goal: After accomplishing basic lane following, we want to upgrade our duckiebot to allow the navigation on twisting courses, and not just simple lines.

Moonshot: The duckiebot will be able to navigate through a maze, avoid moving objects, and/or we will be able to implement our simulation on a physical duckiebot.

## AI/ML algorithms
We will evaluate how different models do in training the duckiebot against each other with an anticipation of Proximal Policy Approximation due to stability issues that may come with other algorithms, with an additional focus in Q-Learning for maze navigation/obstacle avoidance. Generally, we can have our agent start "learning from demonstrations" by training our models with our own ways of walking through obstacles. If we want to possibly expand our project by capturing the states leading up to a crash we could use frame-stacking to potentially avoid any actions that have a higher chance of a duckie crash. For further improvements, we could apply different shortest path algorithms if we want out duckiebot to reach a potential destination within the least amount of time.

## Evaluation Plan
The experiments we are looking to run in order to evaluate the ability of our duckiebot is to judge how fast or how well the duckiebot will do against obstacles in the track, while also not veering from its designated path. Our metrics will be per state could include: a list of close objects (objects that are within a small radius of the duckie bot with attributes including an approximate size, whether they are stationary or not and if so where they are predicted to move), current time, bool hasCrashed, position of duckiebot (coordinates on a map and the orientation of the duckiebot such as angle {to see if our bot is steady on the ground or not}). Per simulation, we can make metrics of the accuracy of predicted crashes, total time taken, or the total number or close calls. 

As for the verification of whether the project proves successful, we can run several hundred simulations accross multiple courses using multiple algorithms. We will find the algorithm that minimizes the total number of crashes and continue using that algorithm to further tweak its parameters using gradient descent. If we have time, we can have another agent or potentially just us that will try to make the duckiebot crash. However it may make our algorithms much more conservative in the sense that it may never move forward and may just use its resources to only avoid obstacles. Essentially a successful duckiebot should avoid all obstacles and find the fastest path to reach its goal. 
what baselines/naive approaches?
how much our approach could improve from baseline

## AI Tool Usage
No AI tools have been used so far.
