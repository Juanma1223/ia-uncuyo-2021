# Cada reina guarda la información de su columna, 
# con los costos asociados a cada posición
class Queen:
    # Este arreglo almacena los valores de la columna de la reina
    # como tuplas que almacena (x y cálculo)
    positions = []
    # Guardamos la mejor posición a la que esta reina puede ir
    bestPos = (0,0,999)
    # Posicion actual de la reina
    x = 0
    y = 0

    def __init__(self,posX,posY):
        self.x = posX
        self.y = posY

    def getPosition(self):
        return (self.x,self.y)

    #Función que calcula la columna de la reina en funcion de las otras
    def calcColumn(self,queens):
        tam = len(queens)
        # Guardamos las posiciones del resto de reinas
        queensPos = []
        for i in range(0,tam):
            queensPos.append(queens[i].getPosition())
        # Calculamos los pares de reinas atacadas para las posiciones de la columna
        for i in range(0,tam):
            self.calcPosition((self.x,i),queensPos)

    #Funcion que calcula la cantidad de reinas atacadas en una posicion específica
    def calcPosition(self,pos,queensPos):
        attacked = 0
        # Recorremos las posiciones de cada reina buscando 
        # reinas atacadas
        tam = len(queensPos)
        for i in range(0,tam):
            # Las reinas nunca van a coincidir en columnas
            if(pos[0] == queensPos[i][0]):
                # Encontramos dos reinas en la misma fila
                attacked = attacked + 2
            if abs(pos[0]-queensPos[i][0]) == abs(pos[1]-queensPos[i][1]):
                # Encontramos dos reinas en la misma diagonal
                attacked = attacked + 2
        # Calculamos el mejor costo
        if(self.bestPos[2] > attacked):
            self.bestPos = (pos[0],pos[1],attacked)
        # Almacenamos el costo de esta posición
        self.positions.append((pos[0],pos[1],attacked))

    def getBestPos(self):
        return self.bestPos

    # Función que retorna las los valores de función de la columna en la 
    # que se encuentra la reina
    def getPositions(self):
        return self.positions

    def move(self,pos):
        self.x = pos[0]
        self.y = pos[1]