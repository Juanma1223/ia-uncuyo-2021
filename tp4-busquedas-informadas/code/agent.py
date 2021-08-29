from math import sqrt
from linked_list import LinkedList
from tree import Node,Tree

class Agent:
    posx = None
    posy = None
    env = None
    #Mantenemos un historial de posiciones recorridas
    explored_set = []

    def __init__(self,posx,posy,env = None):
        self.posx = posx
        self.posy = posy
        self.env = env

    def setEnvironment(self,env):
        self.env = env

    #Implementación del algoritmo A*
    def AStar(self,showSolution = False):
        if(showSolution == True):
            self.env.print_environment()
        #Guardamos las posiciones iniciales para luego imprimirlas
        initX = self.posx
        initY = self.posy
        #En este caso voy a usar las listas nativas de python por una cuestión de legibilidad
        q = []
        #Manejamos tuplas para poder almacenar x e y, ahora también introducimos el peso
        #Para este caso, el peso siempre será 1 por no ser un problema con ponderación
        #Este nodo es parte de la clase Tree, no de LinkedList
        newNode = Node((self.posx,self.posy,self.distancia(self.posx,self.posy)))
        q.append(newNode)
        #Agregamos la posición inicial a los nodos explorados con un 3
        self.env.floor[self.posx][self.posy] = 3
        solution = None
        currNode = q.pop(0)
        while currNode != None:  
            self.posx = currNode.value[0]
            self.posy = currNode.value[1]
            #Verificamos si alcanzamos el objetivo
            if(self.env.floor[self.posx][self.posy] == 2):
                solution = currNode
                break

            #Marcamos esta posición como explorada o negra con un 3
            self.env.floor[self.posx][self.posy] = 3
            #Almacenamos nodos de un arbol, formando un arbol de expansion

            #Encolamos para explorar la posicion superior
            if(self.up(self.posx,self.posy) != False):
                if(self.env.floor[self.posx][self.posy+1] == 2):
                    solution = currNode
                    break
                #Agregamos un nodo al arbol, con nodo padre el nodo actualmente explorado con su respectivo peso
                newNode = Node(self.up(self.posx,self.posy),currNode)
                #Lo marcamos como ya encolado o gris con un 4
                self.env.floor[self.posx][self.posy+1] = 4
                q.append(newNode)
                #Ordenamos la lista según la heurística
                q.sort(key=lambda node : node.value[2])

            #Encolamos para explorar la posicion inferior
            if(self.down(self.posx,self.posy) != False):
                if(self.env.floor[self.posx][self.posy-1] == 2):
                    solution = currNode
                    break
                newNode = Node(self.down(self.posx,self.posy),currNode)
                self.env.floor[self.posx][self.posy-1] = 4
                q.append(newNode)
                q.sort(key=lambda node : node.value[2])

            #Encolamos para explorar la posicion de la izquierda
            if(self.left(self.posx,self.posy) != False):
                if(self.env.floor[self.posx-1][self.posy] == 2):
                    solution = currNode
                    break
                newNode = Node(self.left(self.posx,self.posy),currNode)
                self.env.floor[self.posx-1][self.posy] = 4
                q.append(newNode)
                q.sort(key=lambda node : node.value[2])

            #Encolamos para explorar la posicion de la derecha
            if(self.right(self.posx,self.posy) != False):
                if(self.env.floor[self.posx+1][self.posy] == 2):
                    solution = currNode
                    break
                newNode =  Node(self.right(self.posx,self.posy),currNode)
                self.env.floor[self.posx+1][self.posy] = 4
                q.append(newNode)
                q.sort(key=lambda node : node.value[2])
            
            if(q != []):
                currNode = q.pop(0)
            else:
                #Ya no quedan nodos por recorrer
                break

        if(showSolution == True):
            self.env.print_solution(initX,initY,solution)
        if(solution != None):
            #En este caso la solución también muestra el peso de cada una de las aristas del camino en el 3er
            #atributo de la tupla
            return solution.pathToRoot()
        else:
            return []

    def distancia(self,x,y):
        objX = self.env.get_objX()
        objY = self.env.get_objY()
        distX = abs(x-objX)
        distY = abs(y-objY)
        return sqrt(distX**2 + distY**2)


    #Conjunto de acciones del agente
    def up(self,currX,currY):
        if(currY+1) < self.env.get_sizeY():
            #Verificamos si no se ha explorado ya o es un obstaculo
            if(self.env.floor[currX][currY+1] == 3 or self.env.floor[currX][currY+1] == 1 or self.env.floor[currX][currY+1] == 4):
                return False
            currY += 1
            #Se retorna la posición del siguiente estado y f(n) = g(n) + h(n)
            #En este caso g(n) = 1 y h(n) = distancia entre el objetivo y el nodo explorado
            return (currX,currY,self.distancia(currX,currY+1))
        else:
            #print("No se puede ir hacia arriba")
            return False
    
    def down(self,currX,currY):
            if(currY-1) >= 0:
                #Verificamos si no se ha explorado ya
                if(self.env.floor[currX][currY-1] == 3 or self.env.floor[currX][currY-1] == 1 or self.env.floor[currX][currY-1] == 4):
                    return False
                currY -= 1
                #Retorna
                return (currX,currY,self.distancia(currX,currY-1))
            else:
                #print("No se puede ir hacia abajo")
                return False
    
    def left(self,currX,currY):
        if(currX-1) >= 0:
            #Verificamos si no se ha explorado ya
            if(self.env.floor[currX-1][currY] == 3 or self.env.floor[currX-1][currY] == 1 or self.env.floor[currX-1][currY] == 4):
                return False
            currX -= 1
            return (currX,currY,self.distancia(currX-1,currY))
        else:
            #print("No se puede ir hacia la izquierda")
            return False

    def right(self,currX,currY):
        if(currX+1) < self.env.get_sizeX():
            #Verificamos si no se ha explorado ya
            if(self.env.floor[currX+1][currY] == 3 or self.env.floor[currX+1][currY] == 1 or self.env.floor[currX+1][currY] == 4):
                return False
            currX += 1
            return (currX,currY,self.distancia(currX+1,currY))
        else:
            #print("No se puede ir hacia la derecha")
            return False


    