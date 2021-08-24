#Scripts para calcular las estadísticas para analizar los algoritmos

from random import randint
from environment import Environment
from agent import Agent
import statistics

envSize = 100
posx = randint(0,envSize-1)
posy = randint(0,envSize-1)
a = Agent(posx,posy)
#Pruebas para el algoritmo bfs
resultsBFS = []
for i in range(0,30):
    #El entorno tiene un índice de aparición de obstaculos del 30%
    newEnv = Environment(100,100,0.3)
    a.setEnvironment(newEnv)
    result = a.breadthSearch()
    #Revisar que haya encontrado el objetivo y no haya fallado
    if(result != []):
        resultsBFS.append(newEnv.totalStates())

print(resultsBFS)
print("Media:",statistics.mean(resultsBFS))
print("Desviación estandar:",statistics.stdev(resultsBFS))
print("")

resultsDFS = []
#Pruebas para el algoritmo dfs
for i in range(0,30):
    newEnv = Environment(100,100,0.3)
    a.setEnvironment(newEnv)
    result = a.depthSearch(envSize*5)
    if(result != []):
        resultsDFS.append(newEnv.totalStates())

print(resultsDFS)
print("Media:",statistics.mean(resultsDFS))
print("Desviación estandar:",statistics.stdev(resultsDFS))
print("")

resultsUS = []
#Pruebas para el algoritmo us
for i in range(0,30):
    newEnv = Environment(100,100,0.3)
    a.setEnvironment(newEnv)
    result = a.uniformSearch()
    if(result != []):
        resultsUS.append(newEnv.totalStates())

print(resultsUS)
print("Media:",statistics.mean(resultsUS))
print("Desviación estandar:",statistics.stdev(resultsUS))
print("")


