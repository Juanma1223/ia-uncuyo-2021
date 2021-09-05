from random import randint
from queen import Queen

class Environment:
    queensQuant = 8
    #Arreglo que mantiene las posiciones de las reinas
    queens = []


    def __init__(self,queens = 8):
        self.queensQuant = queens
        # Inicialización del arreglo de reinas
        print("Posiciones iniciales")
        for i in range(0,self.queensQuant):
            # Inicializamos las reinas
            newQueen = Queen(i,randint(0,self.queensQuant-1))
            print(newQueen.getPosition())
            self.queens.append(newQueen)
        # Calculamos costos de las columnas
        for i in range(0,self.queensQuant):
            self.queens[i].calcColumn(self.queens)

    def greedyMove(self):
        # Buscamos el mejor movimiento posible
        tam = len(self.queens)
        bestQueen = None
        bestPos = 999
        for i in range(0,tam):
            currQueen = self.queens[i]
            currQueenPos = currQueen.getBestPos()
            if(currQueenPos[2] <= bestPos):
                # Evitamos que siempre quede en la misma posición
                if(currQueen.getPosition()[0] != currQueenPos[0] or currQueen.getPosition()[1] != currQueenPos[1]):
                    # Guardamos la reina que tiene el mejor movimiento
                    bestQueen = self.queens[i]
                    bestPos = currQueenPos[2]

        # Movemos la reina al mejor estado que encontramos
        if(bestQueen != None):
            posToMove = bestQueen.getBestPos()
            bestQueen.move((posToMove[0],posToMove[1]))
            self.recalculate()
            #Indicamos que siga calculando
            return True
        else:
            return False

    #Recalculamos los costos de cada una de las posiciones
    def recalculate(self):
        tam = len(self.queens)
        for i in range(0,tam):
            self.queens[i].calcColumn(self.queens)

    def printQueens(self):
        tablero = [ [ "*" for _ in range(0,8) ] for _ in range(0,8) ]
        for i in range(0, len(self.queens)):
            currPos = self.queens[i].getPosition()
            tablero[currPos[0]][currPos[1]] = "o"
        for i in range(0, len(self.queens)):
            for j in range(0, len(self.queens)):
                print(tablero[i][j],end="")
            print("")
