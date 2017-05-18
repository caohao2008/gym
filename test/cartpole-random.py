#http://kvfrans.com/simple-algoritms-for-solving-cartpole/
import gym
import numpy as np
import matplotlib.pyplot as plt

def run_episode(env, parameters):
    observation = env.reset()
    totalreward = 0
    for _ in xrange(200):
        action = 0 if np.dot(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward

def run_episode_rend(env, parameters):
    observation = env.reset()
    totalreward = 0
    for _ in xrange(200):
        env.render()
        action = 0 if np.dot(parameters,observation) < 0 else 1
        observation, reward, done, info = env.step(action)
        totalreward += reward
        if done:
            break
    return totalreward


def train(submit):
    env = gym.make('CartPole-v0')
    if submit:
        env.monitor.start('cartpole-experiments/', force=True)

    counter = 0
    bestparams = None
    bestreward = 0
    for _ in xrange(10000):
        counter += 1
        parameters = np.random.rand(4) * 2 - 1
        reward = run_episode(env,parameters)
        if reward > bestreward:
            bestreward = reward
            bestparams = parameters
            if reward == 200:
                break

    if submit:
        for _ in xrange(100):
            run_episode(env,bestparams)
        env.monitor.close()

    return counter,bestparams

# train an agent to submit to openai gym
# train(submit=True)

# create graphs
results = []
bestparams=None
count=0
#for _ in xrange(10):
count,bestparams=train(submit=False)

env = gym.make('CartPole-v0')
run_episode_rend(env,bestparams)

