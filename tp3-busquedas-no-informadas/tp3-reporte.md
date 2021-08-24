# B)

## Algoritmo de búsqueda a lo ancho
### Resultados de aquellos entornos que tienen solución:
[3370, 316, 1688, 4581, 6473, 4345, 1083, 4723, 2950, 4735, 5179, 5423, 4439, 741, 516, 5281, 1240, 4613, 6298, 1293, 2345, 6711, 6518, 855, 272, 1034]
Media: 3347
Desviación estandar: 2219.0013068946128

## Algoritmo de búsqueda en profundidad
### Resultados de aquellos entornos que tienen solución:
[397, 314, 3422, 2717, 5150, 3360, 2001, 845, 3008, 690, 2981, 781, 4068, 207, 1795, 3933, 2979, 1428, 550, 2988]
Media: 2180.7
Desviación estandar: 1472.8453700950845

## Algoritmo de búsqueda uniforme
### Resultados de aquellos entornos que tienen solución:
[2585, 3261, 1, 3783, 2184, 6730, 114, 5701, 4542, 1125, 3011, 2452, 6369, 1479, 5735, 4632, 5488, 296, 2077, 3702, 6457, 193, 2882, 1787, 6363, 1944, 1961]
Media: 3216.814814814815
Desviación estandar: 2134.4133590905926

# C) 
    Para analizar cual de los 3 algoritmos es el mas adecuado para este problema en particular,
    me basé principalmente en 2 medidas de performance: Cantidad de estados recorridos y camino mas corto hallado.


    Por ser un problema cuyos "movimientos" no conllevan un costo, es decir, no representa un grafo ponderado, el algoritmo
    de búsqueda uniforme y búsqueda a lo ancho tienen los mismos resultados.


    En cuanto a la medida de cantidad de estados recoreridos, el algoritmo en profundidad resulta el mas eficiente, esto es debido
    a que no necesariamente va a explorar absolutamente todos los nodos hasta llegar al objetivo, si no que se basa en probar
    caminos hasta que uno de en el blanco, por tanto, es muy probable que encuentre un camino hasta el objetivo antes de recorrer todas las posibilidades. 
    
    Por otro lado, el algoritmo en profundidad revisa absolutamente todas las posiciones en órden de cercanía y por tanto,
    recorre muchos mas estados, eso se observa claramente en la media, ya que generalmente puede recorrer mas de 100 estados
    mas que el algoritmo en profundidad

    Con respecto a la medida del camino mas corto, resulta claro vencedor el algoritmo de búsqueda en profundidad.
    Esto se debe a que busca todos los caminos posibles, analizando siempre los nodos mas cercanos y por tanto, todo camino
    hacia cualquier nodo que descubra será el mas corto.
    Por otro lado, si bien el hecho de limitar la profundidad del camino que encuentre el algoritmo DFS resulta en caminos mas cortos que sin esta limitación, sigue encontrando caminos mas extensos por lógica, es altamente probable que al buscar
    siempre en el nodo recientemente descubierto no se encuentre el camino mas corto (aunque puede suceder), aunque si uno
    relativamente óptimo aunque sifnificativamente mas largo que BFS

    A partir de todo esto, creo que BFS resulta la mejor opción, porque a pesar de recorrer en promedio 1000 estados mas
    que DFS devuelve exactamente el camino mas corto, con una precisión del 100%. Para un problema de tamaño relativamente
    pequeño como este, en el cual estamos recorriendo una cuadrícula de 100x100, resulta pequeña la diferencia en la cantidad
    de estados, 1000 nodos mas por recorrer no resulta un reto para ningún procesador moderna. Sin embargo, si el problema
    escalara a tamaños de masiado grandes, creo que si valdría la pena darle una oportunidad a la reducción de estados que
    nos brinda DFS.