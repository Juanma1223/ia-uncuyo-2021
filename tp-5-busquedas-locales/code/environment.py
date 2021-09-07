from random import randint
from queen import Queen
from math import exp

class Environment:
    queensQuant = 0
    #Arreglo que mantiene las posiciones de las reinas
    queens = []
    #Valor de función actual
    currValue = 0
    #Valor de filtro estadístico actual
    t = 1

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
        self.currValue = 2*queens

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
        if(bestQueen != None and bestPos <= self.currValue):
            posToMove = bestQueen.getBestPos()
            bestQueen.move((posToMove[0],posToMove[1]))
            self.recalculate()
            self.currValue = bestPos
            #Retornamos el valor de la función hacia el que nos movemos
            return bestPos
        else:
            return self.currValue

    def annealing_move(self):
        tam = len(self.queens)
        # Se elije una reina al azar
        randNum = randint(0,tam-1)
        currQueen = self.queens[randNum]
        # Elejimos una posición al azar
        columns = currQueen.getPositions()
        queenColumn = list(filter(lambda pos : pos[0]==randNum,columns))
        currPos = queenColumn[randint(0,tam-1)]
        print(currPos)
        #Verificamos si el valor de la función es menor que el actual
        self.t = self.t + 0.1
        if(currPos[2] <= self.currValue):
            #Nos movemos hacia el nuevo estado
            print("Cambio a mejor estado!")
            self.currValue = currPos[2]
            currQueen.move((currPos[0],currPos[1]))
            self.recalculate()
            return currPos[2]
        else:
            # Calculamos la probabilidad de saltar a un estado peor que el actual
            prob = randint(0,100)/100
            div = exp(abs(currPos[2]-self.currValue)/self.t)/100
            print("div",div)
            print("prob",prob)
            #print(exp(div))
            if(div > prob):
                # Nos movemos hacia el nuevo estado
                print("Cambio random!")
                self.currValue = currPos[2]
                currQueen.move((currPos[0],currPos[1]))
                self.recalculate()
                # Aca se calcula la función de crecimiento de la variable t
                return currPos[2]
            else:
                return self.currValue

    #Recalculamos los costos de cada una de las posiciones
    def recalculate(self):
        tam = len(self.queens)
        for i in range(0,tam):
            self.queens[i].calcColumn(self.queens)

    def printQueens(self):
        tablero = [ [ "*" for _ in range(0,len(self.queens)) ] for _ in range(0,len(self.queens)) ]
        for i in range(0, len(self.queens)):
            currPos = self.queens[i].getPosition()
            tablero[currPos[0]][currPos[1]] = "o"
        for i in range(0, len(self.queens)):
            for j in range(0, len(self.queens)):
                print(tablero[i][j],end="")
            print("")
