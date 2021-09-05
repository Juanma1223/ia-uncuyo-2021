from environment import Environment
from agent import Agent
from random_agent import RandomAgent

#x = int(input("Tamaño:"))
#rate = float(input("Ratio suciedad:"))

#El entorno puede o no ser cuadrado, 
x = 8
print("x:"+ str(x))
#Ratio de aparición de suciedad
rate = 0.6

#El entorno puede, o no, ser cuadrado
#Inicialización de los entornos
env = Environment(x,x,rate)
env2 = Environment(x,x,rate)

#Inicialización del agente aspiradora
agent = Agent(env,1)

#Inicialización del agente aleatorio
rand_agent = RandomAgent(env2,10000)

#Mostramos el entorno en el que está el agente aspiradora
print("Entorno al inicio")
env.print_environment()

#Simulación del tiempo en el agente aspiradora
while(agent.currLife > 0):
    agent.think()

#Simulación del agente aleatorio
while(rand_agent.currLife > 0):
    rand_agent.think()

#Se muestra el entorno luego de la vida útil del agente aspiradora
print("Entorno final")
env.print_environment()

#Se calcula el porcentaje de suciedad en el ambiente
print(env.get_performance())
#Se calcula el performance del agente aspiradora
print(rand_agent.get_performance())

#Se calcula la performance del agente aleatorio
print("Performance del agente aleatorio:",rand_agent.get_performance())