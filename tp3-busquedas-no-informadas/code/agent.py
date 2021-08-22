from linked_list import LinkedList
from tree import Node,Tree

class Agent:
    posx = None
    posy = None
    env = None
    #Mantenemos un historial de posiciones recorridas
    explored_set = []

    def __init__(self,posx,posy,env):
        self.posx = posx
        self.posy = posy
        self.env = env

#Algoritmo de búsqueda a lo ancho, utilizo 0 para posición blanca, 4 para posicion gris y 3 para posición negra
    def breadth_search(self):
        #Guardamos las posiciones iniciales para luego imprimirlas
        initX = self.posx
        initY = self.posy
        #Lista enlazada que funcionará como queue para nodos por visitar
        q = LinkedList()
        #Manejamos tuplas para poder almacenar x e y
        newNode = Node((self.posx,self.posy))
        q.add(newNode)
        #Agregamos la posición inicial a los nodos explorados con un 3
        self.env.floor[self.posx][self.posy] = 3
        solution = None
        while q.head != None:  
            currNode = q.dequeue()
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
                #Verificamos que no sea un nodo ya encolado
                if(self.env.floor[self.posx][self.posy+1] != 4):
                    if(self.env.floor[self.posx][self.posy+1] == 2):
                        solution = currNode
                        break
                    #Agregamos un nodo al arbol, con nodo padre el nodo actualmente explorado
                    newNode = Node(self.up(self.posx,self.posy),currNode)
                    #Lo marcamos como ya encolado o gris con un 4
                    self.env.floor[self.posx][self.posy+1] = 4
                    q.add(newNode)

            #Encolamos para explorar la posicion inferior
            if(self.down(self.posx,self.posy) != False):
                if(self.env.floor[self.posx][self.posy-1] != 4):
                    if(self.env.floor[self.posx][self.posy-1] == 2):
                        solution = currNode
                        break
                    newNode = Node(self.down(self.posx,self.posy),currNode)
                    self.env.floor[self.posx][self.posy-1] = 4
                    q.add(newNode)

            #Encolamos para explorar la posicion de la izquierda
            if(self.left(self.posx,self.posy) != False):
                if(self.env.floor[self.posx-1][self.posy] != 4):
                    if(self.env.floor[self.posx-1][self.posy] == 2):
                        solution = currNode
                        break
                    newNode = Node(self.left(self.posx,self.posy),currNode)
                    self.env.floor[self.posx-1][self.posy] = 4
                    q.add(newNode)

            #Encolamos para explorar la posicion de la derecha
            if(self.right(self.posx,self.posy) != False):
                if(self.env.floor[self.posx+1][self.posy] != 4):
                    if(self.env.floor[self.posx+1][self.posy] == 2):
                        solution = currNode
                        break
                    newNode =  Node(self.right(self.posx,self.posy),currNode)
                    self.env.floor[self.posx+1][self.posy] = 4
                    q.add(newNode)
        print("")
        print("")
        self.env.print_solution(initX,initY,solution)
        return solution.pathToRoot()


#Conjunto de acciones del agente

    def up(self,currX,currY):
        if(currY+1) < self.env.get_sizeY():
            #Verificamos si no se ha explorado ya o es un obstaculo
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


    