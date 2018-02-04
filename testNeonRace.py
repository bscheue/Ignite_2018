import universe
import gym
env = gym.make(‘flashgames.NeonRace-v0’)
env.configure(remotes=1) # creates a local docker container
observation_n = env.reset()
while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
