# Ejercicio 1
Resolución obtenida del libro AIMA 3ra edición, pag 213:

En este caso, se toma en cuenta un sudoku de 9*9

Variables: Las 81 cuadrículas.

Dominio para las cuadrículas con números preasignados: {número preasignado}.

Dominio para las cuadrículas vacías: {1,2,3,4,5,6,7,8,9}

Restricciones:

Para definir las restricciones, se utiliza el operador "AllDiff", el cual define que todos los elementos
que en el se encuentren deben ser diferentes, por ejemplo: AllDiff(A,B,C) => (A != B), (A != C), (B != C).

Se utiliza la nomenclatura A1 hasta A9 para definir la fila superior, B1 hasta B9 para la segunda fila, etc.

Para simbolizar la restricción de que todos los números en misma fila, columna y cuadrícula de 3x3 deben ser distintos escribimos los siguiente:

Fila 1: AllDiff(A1,A2,A3,A4,A5,A6,A7,A8,A9)

Fila 2: AllDiff(B1,B2,B3,B4,B5,B6,B7,B8,B9)

Fila 3: AllDiff(C1,C2,C3,C4,C5,C6,C7,C8,C9)

...

Fila 9: AllDiff(I1,I2,I3,I4,I5,I6,I7,I8,I9)

Columna 1: AllDiff(A1,B1,C1,D1,E1,F1,G1,H1,I1)

Columna 2: AllDiff(A2,B2,C2,D2,E2,F2,G2,H2,I2)

...

Columna 9: AllDiff(A9,B9,C9,D9,E9,F9,G9,H9,I9)

Cuadrícula 1: AllDiff(A1,A2,A3,B1,B2,B3,C1,C2,C3)

Cuadrícula 2: AllDiff(A4,A5,A6,B4,B5,B6,C4,C5,C6)

...

Cuadrícula 9: AllDiff(G7,G8,G9,H7,H8,H9,I7,I8,I9)

# Ejercicio 2

La idea detrás de esta demostración está en la manera en la que se recorren los arcos para verificar la arco consistencia.
Si tan solo aplicamos arco consistencia, rápidamente nos daremos cuenta que esta no detecta todas las inconsistencias entre las variables,
ya que una vez aplicada la arco consistencia, no verificamos la consistencia del resto de variables que pueden haber sido afectadas luego 
de hacer que el nodo actualmente revisado haya obtenido un estado de arco consistencia.

Sin embargo, el algoritmo AC-3 mantiene una cola de todas aquellas variables que han sido modificadas por la arco consistencia, para luego
revisarlas nuevamente en busca de mas inconsistencias.

Para este caso específico del problema de colorear el mapa de australia los pasos serían los siguientes:

Al aplicar la asignación parcial {WA = red, V = blue} tenemos que encolar para revisión a cada una de las variables
cuyos dominios pueden verse afectados al aplicar arco consistencia sobre WA y V, por tanto en la cola nos quedarían:

SA con dominio {green}, NT con dominio {blue, green} y NSW con dominio {red, green}

Luego de desencolar para obtener la arcoconsistencia nos encontraríamos eventualmente con NT o SA,
en los cuales, al aplicar arco consistencia debemos eliminar "green" del dominio de SA, dejándolo sin ninguna asignación posible y resultando
en una solución inconsistente y teniendo que volver hacia atrás en nuestro arbol de solución.

# Ejercicio 3

Para calcular el peor caso de AC-3 se sigue el siguiente razonamiento:

En primer lugar tenemos n variables, con dominios de tamaño d y una cantidad c de restricciones binarias.
Verificar la arco consistencia de una variable se puede realizar en tiempo O(d^2), eso debemos multiplicarlo por la cantidad de restrcciones (ya que debemos verificar cada restricción para cada variable) y luego por la cantidad de valores del dominio nuevamente, dando como resultado para el peor caso: O(c*(d^3)).

# Ejercicio 5

a)

Según el desarrollo del algoritmo CSP para árboles estructurados del libro, tenemos 3 pasos en la resolución:

1) Generar el árbol estructurado de manera tal que el grafo de restricciones se componga únicamente de nodos padre-hijo, dejándonos
con el único problema de resolver arco-consistencia en lugar de n-consistencia 

2) Realizar la arco-consistencia en sentido inverso (de la hoja hacia la raiz), eliminando los valores necesarios de los dominios.

3) Asignar valores válidos del dominio a cada una de las variables.

La idea detrás de estos pasos es la de convertir un problema en la que debemos resolver n-consistencia, en uno en el que solo debemos resolver
arco-consistencias. Gracias al paso 1, en el que convertimos un grafo en un árbol cuyas únicas "relaciones" que encontramos son padre e hijo,
jamás nos hallaremos en la situación de tener que resolver una consistencia mayor que la arco-consistencia, es decir, solo nos encontraremos
con restricciones binarias por la propia naturaleza del árbol. Por tanto, si bien nuestro problema inicial contenía restricciones de mas de
dos variables, luego de la conversión, solo es necesario obtener la arco-consistencia de todas las variables a lo largo del árbol, y por
consecuencia, habremos resuelto las que, en un inicio, fueron restricciones de n variables.

b) Gracias al ejercicio anterior, llegamos a la conclusión de que es posible resolver un CSP cuyo grafo de restricciones es un árbol, mediante
la arco-consistencia de cada una de sus variables, es decir, el algoritmo citado en el ejercicio anterior resulta correcto para todos los
CSP cuyo grafo de restrcciones pueda ser convertido en un árbol, a pesar de que en un principio parezca que tenemos que lidiar con la
n-consistencia. 

# Ejercicio 6

Resultados de las pruebas de 4,8,10,12 y 15 en órden:


Backtracking times: [0.12400031089782715, 0.09799957275390625, 1.5820000171661377, 38.57800078392029, 900]

Backtracking states: [333189, 335028, 355273, 685863, 239500800.0]

Forward checking times: [0.0010004043579101562, 0.012001514434814453, 0.013997793197631836, 0.039000749588012695, 0.24900007247924805]

Forward checking states: [8, 121, 223, 484, 1843]

## Imágenes

[img](https://github.com/Juanma1223/ia-uncuyo-2021/blob/main/tp6-csp/plots/backtracking_states.png)
[img](https://github.com/Juanma1223/ia-uncuyo-2021/blob/main/tp6-csp/plots/backtracking_times.png)
[img](https://github.com/Juanma1223/ia-uncuyo-2021/blob/main/tp6-csp/plots/forward_checking_states.png)
[img](https://github.com/Juanma1223/ia-uncuyo-2021/blob/main/tp6-csp/plots/forward_checking_times.png)
