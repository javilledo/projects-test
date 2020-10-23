import gym

env = gym.make('CartPole-v0')
Rtotal = 0
episodes = 20

for i_episode in range(episodes):
    observation = env.reset()
    R = 0
    action = 1
    for t in range(1000):
        env.render()

        if observation[2] > 0:
            if observation[3] > 0:
                action = 1
            else:
                action = env.action_space.sample()
        else:
            if observation[3] < 0:
                action = 0
            else:
                action = env.action_space.sample()

        # print(observation)
        # action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        R += reward
        if done:
            print("Episode finished after %s timesteps y la recompensa ha sido de %s"% (format(t+1),R))
            Rtotal += R
            break
print("Recompensa media: %s" % str(Rtotal/episodes))
env.close()
