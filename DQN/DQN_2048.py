"""SETTING UP ENVIRONMENT"""

import gymnasium as gym
import gymnasium_2048
from stable_baselines3 import DQN
import numpy as np

class TrainingWrapper(gym.Wrapper):
    def is_legal(self):
        board = self.env.unwrapped.board.copy()
        legal = []
        # Get all legal actions 0-3
        for action in range(4):
            test = board.copy()
            if self.env.unwrapped.is_legal(action):
                legal.append(action)
        return legal
        
    def step(self, action):
        # Get last board state
        # prev_board = self.env.unwrapped.board.copy()
        # Get current board state
        obs, reward, done, truncated, info = self.env.step(action)

        # Punish when stuck on illegal move
        # if np.array_equal(prev_board, obs):
        #     reward -= 100
        if info['is_legal'] == False:
            reward -= 100

        # Reward for legal move
        if info['is_legal'] == True:
            reward += 10

        # Reward higher step_score
        added_score = info['step_score']
        if added_score > 0:
            reward += added_score

        return obs, reward, done, truncated, info

training_env = gym.make("gymnasium_2048:gymnasium_2048/TwentyFortyEight-v0", size=4, max_pow=11)
training_env = TrainingWrapper(training_env)


"""TRAINING WITH DQN"""

model = DQN(
    "MlpPolicy", 
    training_env, 
    learning_rate=1e-2,     
    buffer_size=5000,   
    learning_starts=100,  
    batch_size=16,
    exploration_fraction=0.1, 
    verbose=1
)

print("Training...")
model.learn(total_timesteps=5000)
model.save("dqn_2048_mlp")

del model
model = DQN.load("dqn_2048_mlp")

print("Training finished.")


"""TESTING WITH DQN"""

# Create testing environment
testing_env = gym.make("gymnasium_2048:gymnasium_2048/TwentyFortyEight-v0", size=4, max_pow=11, render_mode="human")
obs, _ = testing_env.reset()
done = False

print("Starting testing.")
while not done:
    testing_env.render()
    
    action, _ = model.predict(obs, deterministic=True)
    
    obs, reward, terminated, truncated, info = testing_env.step(action)
    if info['max'] == 11:
        print("2048 reached!\n")
        break
    # if info['illegal_count'] > 10:
    #     print("Too many bad moves.\n")
    #     break
    if info['is_legal'] == False:
        action = testing_env.action_space.sample()
        obs, reward, terminated, truncated, info = testing_env.step(action)
        # continue
    
    done = terminated or truncated
    # Watch progress
    print(info)

# Print final board state and maximum power
print(f"{info['board']}\nMax = {info['max']}")
print("Game Over")
testing_env.close()
