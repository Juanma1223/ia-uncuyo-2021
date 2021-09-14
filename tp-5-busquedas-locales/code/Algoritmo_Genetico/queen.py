# Clase reducida de reina que representa los genes en el algoritmo genético

class Queen:
    # Posicion actual de la reina
    x = 0
    y = 0
    # Guardamos la cantidad de reinas atacadas por esta reina
    currAttacked = 0
    # BORRAR DESPUES
    env = None

    def __init__(self,posX,posY,env):
        self.x = posX
        self.y = posY
        self.env = env

    def getPosition(self):
        return (self.x,self.y)


    #Funcion que calcula la cantidad de reinas atacadas en la posición actual
    def calcCurrPos(self,queensPos):
        attacked = 0
        pos = (self.x,self.y)
        # Recorremos las posiciones de cada reina buscando 
        # reinas atacadas
        tam = len(queensPos)
        for i in range(0,tam):
            # Las reinas nunca van a coincidir en columnas
            if(pos[1] == queensPos[i][1]):
                # Encontramos dos reinas en la misma fila
                attacked = attacked + 1
            elif abs(pos[0]-queensPos[i][0]) == abs(pos[1]-queensPos[i][1]):
                # Encontramos dos reinas en la misma diagonal
                attacked = attacked + 1
        self.currAttacked = attacked

    def move(self,pos):
        self.x = pos[0]
        self.y = pos[1]