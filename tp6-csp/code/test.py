import backtracking_queens
from tree import Node
import forward_checking
import time
from math import factorial
import matplotlib.pyplot as plt

queens_nums = [4,8,10,12,15]

backTime = []
backStates = []
forwTime = []
forwStates = []

for num in queens_nums:
    dom = [ [ i for i in range(0,num) ] for _ in range(0,num) ]
    root = Node(13,-1,None)
    start = time.time()
    result = forward_checking.dfs(root,dom,num)
    end = time.time()
    forwTime.append((end-start))
    forwStates.append(result[1])

for num in queens_nums:
    start = time.time()
    result = backtracking_queens.dfs(num)
    end = time.time()
    backTime.append((end-start))
    backStates.append(result[1])
    if(num >= 12):
        break

# Valores estimados, los algoritmos no resulven en tiempos coherentes para estos tamaños
backStates.append(factorial(12)/2)
backTime.append(900)

print("Backtracking times",backTime)
print("Backtracking states",backStates)
print("Forward checking times",forwTime)
print("Forward checking states",forwStates)
plt.boxplot(backTime)
plt.title("Tiempo de ejecución backtracking")
plt.show()
plt.boxplot(backStates)
plt.title("Cantidad de estados backtracking")
plt.show()
plt.boxplot(forwTime)
plt.title("Tiempo de ejecución forward checking")
plt.show()
plt.boxplot(forwStates)
plt.title("Cantidad de estados forward checking")
plt.show()