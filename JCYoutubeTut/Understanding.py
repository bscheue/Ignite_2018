import gym
import random
import numpy as np
import atari_py
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean
from collections import Counter


LR = 1e-3 #Just 1 * 10 ^ -3 sci notation
env = gym.make("CartPole-v0") #Chooses the car pole game(or any game)
env.reset() #Resets the enviroment, must be done to set up at start
goal_steps = 500 #Score that we are aiming for, not needed for gym
score_requirement = 50 #minimum score that will be deemed "Successful"
initial_games = 50 #how many games the machine will play for its model

#####################################################################
#This is just a first tester function
# def some_random_games_first():
# 	#each "episode is its own game"
# 	for episode in range(1):
# 		env.reset()
# 		for t in range(200): #this is the time frame allowed for each game
# 			env.render()
# 			#rendering will display the game, but makes it take much much longer
# 			#if the program is taking to long it is most likely due to it trying 
# 			#to render to many things at once.
# 			action = env.action_space.sample()
# 			#This takes all the acceptable actions in the game and chooses one 
# 			#for you. this example uses only two actions

# 			observation, reward, done, info = env.step(action)
# 			#The enviroment then takes the action which it was told to
# 			#It returns these things in this order, all of which are useful
# 			#done is a boolean that will return when the game has ended
# 			if done:
# 				break
# some_random_games_first()
#This funtion will not actuall be used in the learning process
#####################################################################


#####################################################################
#this funtion sets up the data which the model will be based on
def initial_population():
	#[OBS, MOVES]
	#Unsure exactly what this means ATM
	training_data = []
	#all scores
	scores = []
	#the ones that met the minimum
	accepted_scores = []
	#play the amount of games that was previously selected
	# the "_" is normal syntax meaning that the looping variable
	# will not actually be used in the loop. 
	for _ in range(initial_games):
		score = 0 
		# Reinitialize score each game
		game_memory = []
		#remember the moves from this game incase it mets min
		prev_observation = []
		#the previous observation 
		#then actually start the game running through the frames
		for _ in range(goal_steps):
			env.render()
			action = env.action_space.sample()
			#take a random action based on what is available in the game
			#different the the tutorial because this way should be universal
			observation, reward, done, info = env.step(action)
			#remember the observation and coralate it with the action
			game_memory.append([observation,action])
			score+=reward
			if done:break

		if score >= score_requirement:
			accepted_scores.append(score)
			for data in game_memory:
				training_data.append(data[0],data[1])
			# Now The tutorial switches it to binary, Im gonna try and not do that

		env.reset()
		scores.append(score)

	# just in case you wanted to reference later
	training_data_save = np.array(training_data)
	np.save('saved.npy',training_data_save)

	# some stats here, to further illustrate the neural network magic!
	print('Average accepted score:',mean(accepted_scores))
	print('Median score for accepted scores:',median(accepted_scores))
	#print(Counter(accepted_scores))

	return training_data
initial_population()

