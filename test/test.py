import gym
env = gym.make('CartPole-v0')
#env = gym.make('MsPacman-v0')
#env = gym.make('AirRaid-ram-v0')
#env = gym.make('CartPole-v0')
observation = env.reset()
print(env.action_space)
print(env.observation_space)
print(observation)
for i in range(10):
    env.reset()
    total_reward=0
    for j in range(50):
        #env.render()
        print(observation)
        cur_step=env.action_space.sample()
        observation, reward, done, info = env.step(cur_step) # take a random action
        print(cur_step,reward,done,info)
        total_reward = reward+total_reward
        #if(reward==0):
        #    break
    print "total_reward",total_reward
