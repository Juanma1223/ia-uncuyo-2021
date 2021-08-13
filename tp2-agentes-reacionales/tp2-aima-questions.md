# 2.10: 

a) No, ya que sus decisiones se basan única y exclusivamente en su perceprción actual de una 
porción muy reducida de su entorno, por más que se penalizara cada movimiento. Los agentes
reflexivos simples no implementan ningún tipo de modelo para "memorizar" movimientos penalizados
y por tanto, esta modificación no lo haría actuar "mas racionalmente".

b) Entiendo de que el hecho de que tenga un estado, representa una mejora significativa
para poder "entender" la penalización y por tanto mejoraría su "racionalidad", aunque
tampoco se podría considerar una racionalidad perfecta.
Para generar un estado, se podría guardar las posiciones ya recorridas, evitando caer
en las mismas posiciones que ya han sido limpiadas por el agente (o que en su defecto, ya estaban limpias)

c) Con respecto a la respuesta a, si sus decisiones pudieran estar basadas en el conocimiento
de todo el entorno, es decir, poder decidir donde ir en función de lugares sucios adyacentes, por ejemplo,
este sí sería un agente perfectamente racional para este entorno, ya que limpiría perfectamente todo el entorno
gracias a conocer exactamente donde está la suciedad.

En el caso de la respuesta b, la idea de conservar el estado de limpieza de las cuadrículas ya recorridas pierde sentido,
ya que si se conocieran todas las posiciones donde hay suciedad, la implementación mas eficiente sería la de un algoritmo
que genere un grafo y busque los caminos mas cortos entre cuadrículas sucias, así, no se desperdiciarían movimientos y se
limpiarían todas las cuadrículas

# 2.11:

a) Este es un caso similar al anterior, ya que el hecho de tener una porción tan pequeña percibida del entorno (solo la casilla en
la que se encuentra), no resulta un grán cambio el hecho de que el entorno sea aleatorio o no, ya que las acciones serán realizadas
de igual manera, si la casilla actual está limpia el agente la limpiará y si no, el agente se moverá, por lo que estos factores
extra de aleatoriedad y desconocimiento no representan un cambio drástico en la racionalidad del agente en el entorno.

b) Esto está demostrado mediante la implementación contenida en este repositorio. Un agente con comportamiento completamente
aleatorio resulta tener una eficacia cercana al 0%, mientras que el agente de reflejo simple obtuvo un desempeño
nada despreciable en diversos entornos de prueba, por lo tanto, el agente de reflejo simple resulta en todo superior
al agente aleatorio

c) El agente aleatorio se desenvuelve pobremente en entornos de grán tamaño.
Esto es debido a que hay una probabilidad mas baja de que coincida la acción tomada aleatoriamente
"limpiar" con el hecho de que haya suciedad en esa cuadrícula, la mayoría del tiempo el agente se la pasa
"vagando" por el entorno sin limpiar ninguna cuadrícula. Esto se ve reflejado en el programa "main.py" donde
se muestra que en la mayoría de los casos el agente no termina limpiando nada

d) Considero que el hecho de conservar estados, resulta una forma muy útil de guardar información que hace
la toma de decisiones del agente mucho mas eficiente, como es el caso de conocer a todo momento la cuadrícula de
la que venimos, esto nos garantiza que el agente no hará movimientos reiterados entre 2 casillas por ejemplo,
aumentando la probabilidad de ir a una casilla no visitada con anterioridad. Sin embargo, a la hora de probar
el agente en entornos como los implementados en "environment.py", no nos encontraríamos con una gran diferencia
en la performance del agente, ya que si bien este evitaría volver a la casilla inmediatamente pasada, no evita el
hecho de que visitemos casillas ya visitadas que no fueron necesariamente la "recién recorrida", esto se podría mejorar
guardando todas las casillas ya recorridas para intentar evitarlas. En este caso, a la hora de probarlo habrían escenarios
en los que el agente cree haber recorrido todas las casillas cuando esto no es así, ya que podría haber recorrido un "círculo"
y haber ingresado a este, encontradonse en la situación en la cual todas sus casillas adyacentes estarían recorridas y no sabría
hacia donde avanzar. Incluso el último problema tiene solución con alguna implementación para salvaguardar estos casos.
Tanto la versión que guarda solo la posición recorrida en la posicion anterior, como la versión que guarda todas las casillas recorridas representan mejoras de eficiencia, ya que evitan hacer movimientos innecesarios por casillas ya recorridas.