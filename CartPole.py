import gym
import random
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean
from collections import Counter
import time

LR = 1e-3
env = gym.make("CartPole-v0")
env.reset()
goal_steps = 1000
score_requirement = 75
initial_games = 10000


def some_random_games_first():
    for episode in range(50):
        env.reset()
        for t in range(goal_steps):
            env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                break


some_random_games_first()

def initial_population():
    training_data = []  # I'm not EXACTLY sure what this is
    scores = []  # just a list of all the scores that it got over initial_games attempts
    accepted_scores = []  # scores but only the ones that are above score_requirement
    for _ in range(initial_games):
        score = 0
        game_memory = []
        prev_observation = []

        # runs the random action game, stores the observation that corresponds with each action in game_memory
        for _ in range(goal_steps):
            action = random.randrange(0, 2)  # either 0 or 1
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

                if data[1] == 1:
                    output = [0, 1]
                elif data[1] == 0:
                    output = [1, 0]
                training_data.append([data[0], output])
        env.reset()
        scores.append(score)
    training_data_save = np.array(training_data)
    np.save('save.npy', training_data_save)  #saves the training data to this file, will overwrite so be careful

    print('Average accepted score:', mean(accepted_scores))
    print('Median accepted score:', median(accepted_scores))
    print(Counter(accepted_scores))
    #print (training_data)
    return training_data


def neural_network_model(input_size):
    network = input_data(shape=[None, input_size, 1], name='input')

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

    network = fully_connected(network, 2, activation='softmax')
    network = regression(network, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(network, tensorboard_dir='log')

    return model


def train_model(training_data, model= False):
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]), 1)  # these are the observations
    y = [i[1] for i in training_data]
    print(X[:10])
    print(y[:10])
    if not model:
        model = neural_network_model(input_size=len(X[0]))

    model.fit({'input': X}, {'targets': y}, n_epoch=3, snapshot_step=500, show_metric=True)

    return model
def train_model2(training_data, model3= False):
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]), 1)  # these are the observations
    y = [i[1] for i in training_data]
    print (X[:10])
    print (y[:10])

    if not model3:
        model3 = neural_network_model(input_size=len(X[0]))

    model3.fit({'input': X}, {'targets': y}, n_epoch=3, snapshot_step=500, show_metric=True)

    return model3
training_data = initial_population()


start = time.time()


modell = train_model(training_data)

print ("THE TIME TO TRAIN THIS NETWORK IS",time.time()-start)
print()
print()
print()
print()
print()
print()
print()
modell.save('laskjdflkj.model')

#model.load('laskjdflkj.model')
def play_games(model):

    training_data = []  # I'm not EXACTLY sure what this is
    scores = []  # just a list of all the scores that it got over initial_games attempts
    accepted_scores = []  # scores but only the ones that are above score_requirement
    choices = []
    for _ in range(5):
        score = 0
        game_memory = []
        prev_observation = []

        # runs the random action game, stores the observation that corresponds with each action in game_memory
        for _ in range(goal_steps):
            env.render()
            if len(prev_observation) == 0:
                action = random.randrange(0, 2)
            else:
                action = np.argmax(
                    model.predict(prev_observation.reshape(-1, len(prev_observation), 1))[0])  # don't understand, look into later
            choices.append(action)

            new_observation, reward, done, info = env.step(action)
            prev_observation = new_observation
            score += reward
            if done:
                break

            if len(prev_observation) > 0:
                game_memory.append([prev_observation, action])

            prev_observation = new_observation

            score += reward
            if done:
                break

        # formats the results a bit better based on what the action was, make sure to change when there's more than one action possibility

        env.reset()
        scores.append(score)

    print ('Average Score', sum(scores)/len(scores))
    print ('Choice 1: {}, Choice 0: {}'.format(choices.count(1)/len(choices),choices.count(0)/len(choices)))
def get_more_data(model):
    training_data = []  # I'm not EXACTLY sure what this is
    scores = []  # just a list of all the scores that it got over initial_games attempts
    accepted_scores = []  # scores but only the ones that are above score_requirement
    choices = []
    for i in range(10000):
        score = 0
        game_memory = []
        prev_observation = []
        print (i)
        # runs the random action game, stores the observation that corresponds with each action in game_memory
        for _ in range(goal_steps):
            if len(prev_observation) == 0:
                action = random.randrange(0, 2)
            else:
                action = np.argmax(
                    model.predict(prev_observation.reshape(-1, len(prev_observation), 1))[0])  # don't understand, look into later
            choices.append(action)

            new_observation, reward, done, info = env.step(action)
            prev_observation = new_observation
            score += reward
            if done:
                break

            if len(prev_observation) > 0:
                game_memory.append([prev_observation, action])

            prev_observation = new_observation

            score += reward
            if done:
                break

        # formats the results a bit better based on what the action was, make sure to change when there's more than one action possibility
        if score >= 350:
            accepted_scores.append(score)
            for data in game_memory:

                if data[1] == 1:
                    output = [0, 1]
                elif data[1] == 0:
                    output = [1, 0]
                training_data.append([data[0], output])
        env.reset()
        scores.append(score)
    training_data_save = np.array(training_data)
    print(len(training_data))
    print('Average accepted score:', mean(accepted_scores))
    print('Median accepted score:', median(accepted_scores))
    print(Counter(accepted_scores))
    return training_data


play_games(modell)


print("\n\n\nplaying more games\n\n\n")

#new_data = get_more_data(modell)
print("\n\n\ntraining new model\n\n\n")
#training_data = get_more_data(modell)
print("\n\n\n\nt2\n\n\n\n")
#np.save('test2.npy', training_data)

#print(t2[:10])
#model2 = train_model2(training_data)
#print("testing")
#play_games(model2)

