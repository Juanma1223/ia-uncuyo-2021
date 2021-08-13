from environment import Environment
from agent import Agent

#x = int(input("Tamaño:"))
x = 128
print("x:"+ str(x))
rate = float(input("Ratio suciedad:"))

env = Environment(x,x,rate)
agent = Agent(env,1000)

print("Entorno al inicio")
env.print_environment()
#Paso del tiempo
while(agent.currLife > 0):
    agent.think()

print("Entorno final")
env.print_environment()
print(env.get_performance())
print(agent.get_performance())