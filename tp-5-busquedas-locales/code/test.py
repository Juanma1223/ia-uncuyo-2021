from environment import Environment
import time
from statistics import mean
from statistics import stdev
import matplotlib.pyplot as plt

print("Resultados con Hill Climbing:")
print("")
# Cantidad de veces que se llega a una solución óptima
HC = 0
timeHistory = []
HCStates = []
queens = 8
intentos = 60
results = []
for j in range(0,intentos):
    env = Environment(queens)
    results = []
    start = time.time()
    for i in range(0,50):
        currVal = env.greedyMove()
        results.append(currVal)
        if(currVal == 0):
            HCStates.append(i)
            break
    last = results.pop()
    end = time.time()
    if(last == 0):
        #env.printQueens()
        HC = HC+1
        timeHistory.append(end-start)
        results.append(last)
        plt.plot(results)
        plt.title("Variación de la función HC")
        plt.show()

if(len(HCStates) >= 2):
    print("Media de tiempo de resolución:", mean(timeHistory))
    print("")
    print("Desviación estandar de tiempo de resolución:", stdev(timeHistory))
    print("")
    print("Porcentaje de soluciones óptimas:",(HC/30)*100)
    print("")
    print("Media de estados por resolución:",mean(HCStates))
    print("")
    print("Desviación estandar de estados por resolución:",stdev(HCStates))
else:
    print("No se encontró ninguna solución!")

print("")
print("###########################################################################")
print("")
print("Resultados con Simulated Anealing:")
print("")
SA = 0
timeHistory = []
SAStates = []
for j in range(0,intentos):
    env = Environment(queens)
    results = []
    start = time.time()
    for i in range(0,200):
        currVal = env.annealing_move()
        results.append(currVal)
        if(currVal == 0):
            SAStates.append(i)
            break
        #env.printQueens()
    last = results.pop()
    end = time.time()
    # Ingresa a un estado óptimo
    if(last == 0):
        #env.printQueens()
        SA = SA + 1
        timeHistory.append(end-start)
        results.append(last)
        plt.plot(results)
        plt.title("Variación de la función SA")
        plt.show()
        #print(results)

if(len(SAStates) >= 2):
    print("Media de tiempo de resolución:", mean(timeHistory))
    print("")
    print("Desviación estandar de tiempo de resolución:", stdev(timeHistory))
    print("")
    print("Porcentaje de soluciones óptimas:",(SA/30)*100)
    print("")
    print("Media de estados por resolución:",mean(SAStates))
    print("")
    print("Desviación estandar de estados por resolución:",stdev(SAStates))
else:
    print("No se encontró ninguna solución!")