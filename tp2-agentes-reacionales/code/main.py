from environment import Environment
from agent import Agent

env = Environment(4,4)
agent = Agent(env)

print("Entorno al inicio")
env.print_environment()
#Paso del tiempo
while(agent.currLife > 0):
    agent.think()

print("Entorno final")
env.print_environment()
print(env.get_performance())
print(agent.get_performance())