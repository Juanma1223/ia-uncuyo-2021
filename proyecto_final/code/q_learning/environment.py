# Class that represents the environment the agent is going to be in

# This first environment approach will generate an objective position which the agent must reach
# Touching the walls will end the episode
# Rewards are to be defined yet

import numpy as np
from random import randint

class Environment:

    # Constructor
    # int obstacles: obstacles quantity
    # int lenth: environment side length
    def __init__(self,obstacles,length):
        self.obstacles = obstacles
        self.length = length
        # Create squared matrix to represent the environment
        self.environment = np.zeros((self.length,self.length))
        self.objectiveX = randint(0,self.length)
        self.objectiveY = randint(0,self.length)
        # Identify objective position with number 5 on our matrix
        self.environment[self.objectiveX,self.objectiveY] = 5

        # Generate agent initial position
        self.agentX = randint(0,self.length)
        self.agentY = randint(0,self.length)


    # Print environment state
    def printEnv(self):
        for i in range(0,self.length):
            for j in range(0,self.length):
                print(self.environment[i,j], end="")
            print("")


    # This function represents de interface of the environment to the agent
    # string action: 4 options, up, left, right and down
    def nextStep(self, action):

        # Implement borders hit if agent reaches the limit

        # Move the agent upwards
        if(action == "up"):
            self.agentY -= 1
        elif(action == "down"):
            self.agentY += 1
        elif(action == "left"):
            self.agentX -= 1
        elif(action == "right"):
            self.agentX += 1

        # Return 3 values:
        # 1) New state the agent is in
        # 2) Reward the agent receives for being in the new state
        # 3) If it has won or lost for either crashing or reaching the objective

        # States are to be defined yet


    def getLength(self):
        return self.length
    