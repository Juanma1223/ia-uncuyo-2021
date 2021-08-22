from random import randint
from tree import Node

#Clase que representa el entorno en el que se mueve el agente buscador
class Environment:
    floor = [[]]
    sizeX = 0
    sizeY = 0
    #Coordenadas del objetivo
    objX = None
    objY = None

    #Inicializamos el entorno con suciedad aleatoria y fijamos el tamaño
    def __init__(self,sizeX,sizeY,obstable_rate):
        #Inicializacion de la lista por comprension
        self.floor = [ [ 0 for _ in range(sizeX) ] for _ in range(sizeY) ]
        for i in range(0,sizeX):
            for j in range(0,sizeY):
                is_dirty = randint(1,10)
                if(is_dirty <= obstable_rate*10):
                    self.floor[i][j] = 1
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.objX = randint(0,sizeX-1)
        self.objY = randint(0,sizeY-1)
        #Marcamos el objetivo en el suelo con un 2
        self.floor[self.objX][self.objY] = 2
        

    def get_sizeX(self):
        return self.sizeX

    def get_sizeY(self):
        return self.sizeY

    def get_objX(self):
        return self.objX

    def get_objY(self):
        return self.objY

    #Preguntamos si hay un obstaculo
    def is_clear(self,x,y):
        try:
            if(self.floor[x][y] == 1):
                return True
            else:
                return False
        except:
            print("",end="")
    
    def print_environment(self):
        tam = len(self.floor)
        for i in range(0, tam):
            print(*self.floor[i])
            print("")

    #Imprimimos de manera mas estética el entorno, se ve mejor en terminales nativas de los SOs
    def print_solution(self,agentX,agentY,last_node):
        #Limpiamos el trablero
        for i in range(0,self.sizeX):
            for j in range(0,self.sizeY):
                if(self.floor[i][j] == 2):
                    self.floor[i][j] = '\u003F'
                elif(self.floor[i][j] == 1):
                    self.floor[i][j] = '\u0048'
                else:
                    self.floor[i][j] = " "
        #Obtenemos el camino solucion
        solution = last_node.pathToRoot()
        for pos in solution:
            self.floor[pos[0]][pos[1]] = '\u006F'
        self.floor[agentX][agentY] = '\u0040'
        self.print_environment()