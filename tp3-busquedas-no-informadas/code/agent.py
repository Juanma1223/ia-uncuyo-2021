from linked_list import LinkedList
from os import system
import copy
import time

class Agent:
    posx = None
    posy = None
    env = None

    def __init__(self,posx,posy,env):
        self.posx = posx
        self.posy = posy
        self.env = env

    def breadth_search(self):
        #Lista enlazada que funcionará como queue para lugares por visitar
        q = LinkedList()
        #Manejamos tuplas para poder almacenar x e y
        q.add((self.posx,self.posy))
        #Agregamos la posición inicial a los nodos explorados con un 3
        self.env.floor[self.posx][self.posy] = 3
        return self.breadth_search_r(q,[])

    def breadth_search_r(self,q,currPath):
        if(q.head == None):
            return []
        currPos = q.dequeue()
        if(self.env.floor[currPos[0]][currPos[1]] != 3):
            currPath.append(currPos)
        self.posx = currPos[0]
        self.posy = currPos[1]
        #Caso base en el cual no hay solución
        #Caso base en el que se encuentra el objetivo
        if(self.env.floor[self.posx][self.posy] == 2):
            return currPath
        else:     
            #Marcamos esta posición como explorada
            self.env.floor[self.posx][self.posy] = 3
            #Encolamos para explorar la posicion superior
            if(self.up(self.posx,self.posy) != False):
                q.add(self.up(self.posx,self.posy))

            #Encolamos para explorar la posicion inferior
            if(self.down(self.posx,self.posy) != False):
                q.add(self.down(self.posx,self.posy))

            #Encolamos para explorar la posicion de la izquierda
            if(self.left(self.posx,self.posy) != False):
                q.add(self.left(self.posx,self.posy))

            #Encolamos para explorar la posicion de la derecha
            if(self.right(self.posx,self.posy) != False):
                q.add(self.right(self.posx,self.posy))
            #clear = lambda: system('cls')
            #clear()
            #self.env.print_environment()
            #time.sleep(0.5)
            return self.breadth_search_r(q,copy.deepcopy(currPath))


    def up(self,currX,currY):
        if(currY+1) < self.env.get_sizeY():
            #Verificamos si no se ha explorado ya
            if(self.env.floor[currX][currY+1] == 3 or self.env.floor[currX][currY+1] == 1):
                return False
            currY += 1
            return (currX,currY)
        else:
            #print("No se puede ir hacia arriba")
            return False
    
    def down(self,currX,currY):
            if(currY-1) >= 0:
                #Verificamos si no se ha explorado ya
                if(self.env.floor[currX][currY-1] == 3 or self.env.floor[currX][currY-1] == 1):
                    return False
                currY -= 1
                return (currX,currY)
            else:
                #print("No se puede ir hacia abajo")
                return False
    
    def left(self,currX,currY):
        if(currX-1) >= 0:
            #Verificamos si no se ha explorado ya
            if(self.env.floor[currX-1][currY] == 3 or self.env.floor[currX-1][currY] == 1):
                return False
            currX -= 1
            return (currX,currY)
        else:
            #print("No se puede ir hacia la izquierda")
            return False

    def right(self,currX,currY):
        if(currX+1) < self.env.get_sizeX():
            #Verificamos si no se ha explorado ya
            if(self.env.floor[currX+1][currY] == 3 or self.env.floor[currX+1][currY] == 1):
                return False
            currX += 1
            return (currX,currY)
        else:
            #print("No se puede ir hacia la derecha")
            return False


    