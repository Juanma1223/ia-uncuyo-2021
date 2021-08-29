#Scripts para calcular las estadísticas para analizar los algoritmos

from random import randint
from environment import Environment
from agent import Agent
import statistics

envSize = 100
posx = randint(0,envSize-1)
posy = randint(0,envSize-1)
a = Agent(posx,posy)

resultsUS = []
for i in range(0,30):
    newEnv = Environment(100,100,0.3)
    a.setEnvironment(newEnv)
    result = a.AStar()
    if(result != []):
        resultsUS.append(newEnv.totalStates())

print(resultsUS)
print("Media:",statistics.mean(resultsUS))
print("Desviación estandar:",statistics.stdev(resultsUS))
print("")


