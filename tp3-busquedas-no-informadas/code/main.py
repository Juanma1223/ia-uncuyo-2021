from random import randint
from environment import Environment
from agent import Agent

envSize = 100
env = Environment(envSize,envSize,0.3)
env.print_environment()
print("")
print("")
posx = randint(0,envSize-1)
posy = randint(0,envSize-1)
print("Posicion inicial del agente: ",posx,", ",posy)
agent = Agent(posx,posy,env)
print("Camino hacia el objetivo")
print(agent.breadth_search())