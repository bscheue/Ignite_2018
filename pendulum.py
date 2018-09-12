import gym
from random import *
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean
from collections import Counter
import time
import copy
import random

LR = 1e-9
env = gym.make("Pendulum-v0")
env.reset()
goal_steps = 1000
score_requirement = -1000
initial_games = 10000

Intervals = [i/100 for i in range(-200,200)]

def some_random_games_first():
    for episode in range(5):
        env.reset()
        for t in range(goal_steps):
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                break

print()
print()
#print("Doing a few test runs")
some_random_games_first()

def initial_population():
    training_data = []  # I'm not EXACTLY sure what this is
    scores = []  # just a list of all the scores that it got over initial_games attempts
    accepted_scores = []  # scores but only the ones that are above score_requirement
    for i in range(initial_games):
        #print (i)
        score = 0
        game_memory = []
        prev_observation = []
        #env.render()
        # runs the random action game, stores the observation that corresponds with each action in game_memory
        for _ in range(goal_steps):
            action = [random.choice(Intervals)]
            # for j in range(len(action)):
            #     action[j] = action[j]/100
            #action = [randint(-200,200)/100]  # either 0 or 1
            observation, reward, done, info = env.step(action)

            if len(prev_observation) > 0:
                game_memory.append([prev_observation, action])

            prev_observation = observation

            score += reward
            if done:
                break

        # formats the results a bit better based on what the action was, make sure to change when there's more than one action possibility
        if score >= score_requirement:
             accepted_scores.append(score)
             for data in game_memory:
                 output = [0 for k in range(400)]
                 #print(data[1][0],data[1][0]*100+200)
                 output[int(data[1][0]*100+200)]=1
                 # if data[1] == 1:
                 #     output = [0, 1]
                 # elif data[1] == 0:
                 #     output = [1, 0]
                 training_data.append([data[0], output])

        env.reset()
        scores.append(score)
    training_data_save = np.array(training_data)
    np.save('save.npy', training_data_save)  #saves the training data to this file, will overwrite so be careful

    print('Average accepted score:', mean(accepted_scores))
    print('Median accepted score:', median(accepted_scores))
    print(Counter(accepted_scores))

    return training_data


def neural_network_model(input_size):
    network = input_data(shape=[None, 3, 1], name='input')

    network = fully_connected(network, 128, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 512, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 256, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 128, activation='relu')
    network = dropout(network, 0.8)

    network = fully_connected(network, 400, activation='softmax')
    network = regression(network, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(network, tensorboard_dir='log')

    return model


def train_model(training_data, model=False):
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]), 1)  # these are the observations
    y = [i[1] for i in training_data]
    #print (y[:20])

    if not model:
        model = neural_network_model(input_size=len(X[0]))

    model.fit({'input': X}, {'targets': y}, n_epoch=5, snapshot_step=500, show_metric=True)

    return model
print ("\n\n\n\n\n\n\n\n\n getting training data")

training_data = initial_population()
print (training_data[:5])
start = time.time()
print()
print()
print()
print()
print()
print("starting training")
model = train_model(training_data)

print ("THE TIME TO TRAIN THIS NETWORK IS",time.time()-start)
print()
print()
print()
print()
print()
print()
print()
#model.save('connect4.model')

#model.load('connect4.model')


scores = []
choices = []

for each_game in range(10):
    score = 0
    game_memory = []
    prev_obs = []
    env.reset()
    for _ in range(goal_steps):
        env.render()
        if len(prev_obs) == 0:
            rrr = random.choice(Intervals)
            action = [rrr]
            print (rrr)
        else:
            action = [Intervals[np.argmax(model.predict(prev_obs.reshape(-1, len(prev_obs), 1)))]]
            # print (action,model.predict(prev_obs.reshape(-1,len(prev_obs),1)),(np.argmax(model.predict(prev_obs.reshape(-1,len(prev_obs),1))[0])))
            print(action, (np.argmax(model.predict(prev_obs.reshape(-1, len(prev_obs), 1))[0])))





        choices.append(action)


        new_observation,reward,done,info = env.step(action)
        #print (prev_obs,new_observation)
        prev_obs = np.array(new_observation)
        game_memory.append([new_observation, action])
        score+=reward
        if done:
            break
    scores.append(score)
print ('Average Score', sum(scores)/len(scores))
print ('Choice 1: {}, Choice 0: {}'.format(choices.count(1)/len(choices),choices.count(0)/len(choices)))