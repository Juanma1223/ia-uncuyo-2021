import numpy as np
import gym
import snake_env as senv

# env = gym.make("FrozenLake-v1")
env = senv.Snake()
n_observations = env.observation_space.n
n_actions = env.action_space.n

#Initialize the Q-table to 0
Q_table = np.zeros((n_observations**3,n_actions))
print(Q_table)

#number of episode we will run
n_episodes = 1000

#maximum of iteration per episode
# max_iter_episode = 100

#initialize the exploration probability to 1
exploration_proba = 1

#exploartion decreasing decay for exponential decreasing
# exploration_decreasing_decay = 0.001
exploration_decreasing_decay = 0.005

# minimum of exploration proba
min_exploration_proba = 0.01

#discounted factor
# gamma = 0.99
gamma = 0.95

#learning rate
# lr = 0.1
lr = 0.00025

rewards_per_episode = list()

#we iterate over episodes
for e in range(n_episodes):
    #we initialize the first state of the episode
    current_state = env.reset()
    done = False
    
    #sum the rewards that the agent gets from the environment
    total_episode_reward = 0
    print('episode ',e)
    while(not (done)): 
        # we sample a float from a uniform distribution over 0 and 1
        # if the sampled flaot is less than the exploration proba
        #     the agent selects arandom action
        # else
        #     he exploits his knowledge using the bellman equation 
        
        if np.random.uniform(0,1) < exploration_proba:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q_table[current_state,:])
        
        # The environment runs the chosen action and returns
        # the next state, a reward and true if the epiosed is ended.
        next_state, reward, done, _ = env.step(action)
        
        # We update our Q-table using the Q-learning iteration
        Q_table[current_state, action] = (1-lr) * Q_table[current_state, action] +lr*(reward + gamma*max(Q_table[next_state,:]))
        total_episode_reward = total_episode_reward + reward
        # If the episode is finished, we leave the for loop
        # if done:
        #     break
        if reward > 1:
            print('recomp_tot ',total_episode_reward)
        current_state = next_state
    #We update the exploration proba using exponential decay formula 
    exploration_proba = max(min_exploration_proba, np.exp(-exploration_decreasing_decay*e))
    rewards_per_episode.append(total_episode_reward)
#TODO
# imprimir Qtable, esta cambiando para mal?
# verificar el vector de estados esta asignando bien los valores?
# modificar el output
print("Mean reward per thousand episodes")
for i in range(n_episodes):
    print("life ",(i+1),": mean espiode reward: ",
           np.mean(rewards_per_episode[i:(i+1)])) 
