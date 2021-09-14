# Clase que representa a un individuo de la población
from queen import Queen
from random import randint

class Individual:

    queensQuant = 0
    # Las variables o genes son las posiciones de las reinas
    queens = []
    fitness = 0

    def __init__(self,queens):
            self.queensQuant = queens
            self.queens = []
            # Inicialización del arreglo de reinas
            for i in range(0,self.queensQuant):
                # Inicializamos las reinas
                newQueen = Queen(i,randint(0,self.queensQuant-1),self)
                #print(newQueen.getPosition())
                self.queens.append(newQueen)

    def getFitness(self):
        # Por la naturaleza del problema, un valor mas alto
        # representa un peor individuo, invertimos eso
        self.calcFitness()
        return ((len(self.queens)**2)-self.fitness)

    def calcFitness(self):
        attacked = 0
        queenPos = []
        for queen in self.queens:
            queenPos.append(queen.getPosition())
        # Calcular la cantidad de reinas atacadas por una reina específica
        for queen in self.queens:
            queen.calcCurrPos(queenPos)
            attacked += queen.currAttacked
        self.fitness = (attacked)

    def getQueens(self):
        return self.queens

    def printQueens(self,debugPos = None):
        tablero = [ [ "*" for _ in range(0,len(self.queens)) ] for _ in range(0,len(self.queens)) ]
        #Marcamos la posición actualmente explorada para debuggear
        if(debugPos != None):
            tablero[debugPos[0]][debugPos[1]] = "-"
        for i in range(0, len(self.queens)):
            currPos = self.queens[i].getPosition()
            tablero[currPos[0]][currPos[1]] = "o"
        for i in range(0, len(self.queens)):
            for j in range(0, len(self.queens)):
                print(tablero[i][j],end="")

            print("")
