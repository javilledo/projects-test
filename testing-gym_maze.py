import sys
#https://github.com/MattChanTK/gym-maze

import numpy as np
import math
import random

import gym
import gym_maze

# Initialize the "maze" environment
env = gym.make("maze-random-10x10-plus-v0")

for i in range(1000):
    # Render tha maze
    env.render()
