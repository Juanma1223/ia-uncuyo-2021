from math import e
from environment import Environment
from agent import Agent

env = Environment(10,10,0.3)
env.print_environment()
agent = Agent(1,1,env)
print(agent.breadth_search())
env.print_environment()

