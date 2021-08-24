from random import randint
from environment import Environment
from agent import Agent

#Funcionamiento de la búsqueda a lo ancho
envSize = 100
#envSize = int(input("Ingrese el tamaño del entorno:"))
env = Environment(envSize,envSize,0.3)
print("")
#env.print_environment()
print("")
print("")
posx = randint(0,envSize-1)
posy = randint(0,envSize-1)
print("Posicion inicial del agente: ",posx,", ",posy)
print("@=Agente, o=Camino, H=Obstaculo, ?=Objetivo")
agent = Agent(posx,posy,env)
print("Camino hacia el objetivo")
print(agent.breadthSearch())
#print(agent.depthSearch(envSize*5))
#print(agent.uniformSearch())
