import matplotlib.pyplot as plt

eje_x = ['BFS', 'DFS', 'US', 'A*']
 
## Valores de la media
eje_y = [3347,2180,3216,119]
 
## Creamos Gráfica
plt.bar(eje_x, eje_y)
 
## Legenda en el eje y
plt.ylabel('Media de estados')
 
## Legenda en el eje x
plt.xlabel('Algoritmos')
 
## Título de Gráfica
plt.title('Media de estados recorridos por algoritmo')
 
## Mostramos Gráfica
plt.show()