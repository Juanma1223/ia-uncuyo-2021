from environment import Environment
import time
from statistics import mean
from statistics import stdev
import matplotlib.pyplot as plt

solutions = []
states = []
timeHistory = []
func = []

for i in range(0,30):
    env = Environment(8,200)
    # Cantidad de estados
    j = 0
    start = time.time()
    for n in range(0,30):
        env.newGeneration()
        #print("")
        #env.printPopulation()
        sol = env.getBestSolution()
        print(sol.getFitness())
        func.append(sol.getFitness())
        if(sol.getFitness() >= 56):
            sol.printQueens()
            solutions.append(sol)
            states.append(j)
            end = time.time()
            timeHistory.append(end-start)
            break
        j += 1

plt.boxplot(timeHistory)
plt.title("Tiempo de resolución GA")
plt.xlabel("Función de fitness (56 es óptimo)")
plt.show()

print("Algoritmo Genético")

print("Media de tiempo de resolución:", mean(timeHistory))
print("")
print("Desviación estandar de tiempo de resolución:", stdev(timeHistory))
print("")
print("Porcentaje de soluciones óptimas:",(len(solutions)/30)*100)
print("")
print("Media de estados por resolución:",mean(states))
print("")
print("Desviación estandar de estados por resolución:",stdev(states))