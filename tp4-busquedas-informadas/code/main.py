from random import randint
from environment import Environment
from agent import Agent
import statistics

#Funcionamiento de los diversos algoritmos
envSize = 50
#envSize = int(input("Ingrese el tamaño del entorno:"))
env = Environment(envSize,envSize,0.3)
posx = randint(0,envSize-1)
posy = randint(0,envSize-1)
print("Posicion inicial del agente: ",posx,", ",posy)
agent = Agent(posx,posy,env)
print(agent.AStar(True))
