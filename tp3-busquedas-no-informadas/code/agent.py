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

    #Algoritmo de búsqueda a lo ancho, utilizo 0 para posición blanca, 4 para posicion gris y 3 para posición negra
    def breadthSearch(self,showSolution = False):
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
                if(self.env.floor[self.posx][self.posy-1] == 2):
                    solution = currNode
                    break
                newNode = Node(self.down(self.posx,self.posy),currNode)
                self.env.floor[self.posx][self.posy-1] = 4
                q.add(newNode)

            #Encolamos para explorar la posicion de la izquierda
            if(self.left(self.posx,self.posy) != False):
                if(self.env.floor[self.posx-1][self.posy] == 2):
                    solution = currNode
                    break
                newNode = Node(self.left(self.posx,self.posy),currNode)
                self.env.floor[self.posx-1][self.posy] = 4
                q.add(newNode)

            #Encolamos para explorar la posicion de la derecha
            if(self.right(self.posx,self.posy) != False):
                if(self.env.floor[self.posx+1][self.posy] == 2):
                    solution = currNode
                    break
                newNode =  Node(self.right(self.posx,self.posy),currNode)
                self.env.floor[self.posx+1][self.posy] = 4
                q.add(newNode)
        #El tercer elemento de la tupla de coordenadas es el peso de la arista
        #para este algoritmo es irrelevante
        if(showSolution == True):
            print("")
            print("")
            self.env.print_solution(initX,initY,solution)
        #Preguntamos si se encontró una solución
        if(solution != None):
            return solution.pathToRoot()
        else:
            return []

    #Algoritmo de búsqueda en profundidad limitada, l es la profundidad máxima
    def depthSearch(self,l,showSolution = False):
        initX = self.posx
        initY = self.posy
        #Creamos el nodo raiz del árbol de expansión
        root = Node((initX,initY))
        solution = self.depthSearchR(l,0,root)
        if(solution != False):
            if(showSolution == True):
                self.env.print_solution(initX,initY,solution.parent)
            return solution.pathToRoot()
        else:
            return []

    #l representa la máxima  profundidad, currL representa la profundidad del nodo actual
    #currNode representa el nodo que se está explorando actualmente
    def depthSearchR(self,l,currL,currNode):
        #Se alcanza la profundidad máxima
        if(currL >= l):
            return False
        #Revisamos si se alcanzó el objetivo
        if(self.env.floor[currNode.value[0]][currNode.value[1]] == 2):
            return currNode
        else:
            solution = False
            #Actualizamos el estado
            #self.posx = currNode.value[0]
            #self.posy = currNode.value[1]
            #Marcamos el estado como ya explorado
            self.env.floor[currNode.value[0]][currNode.value[1]] = 3
            #Si se puede avanzar por arriba, avanzar
            newPos = self.up(currNode.value[0],currNode.value[1])
            if(newPos != False):
                #Creamos el nodo que representa el nuevo estado del agente y lo agregamos al árbol
                #con el estado actual como su padre
                newNode = Node(newPos,currNode)
                solution = self.depthSearchR(l,currL+1,newNode)
                if(solution != False):
                    return solution
                
            newPos = self.down(currNode.value[0],currNode.value[1])
            if(newPos != False):
                #Creamos el nodo que representa el nuevo estado del agente y lo agregamos al árbol
                #con el estado actual como su padre
                newNode = Node(newPos,currNode)
                solution = self.depthSearchR(l,currL+1,newNode)
                if(solution != False):
                    return solution

            newPos = self.left(currNode.value[0],currNode.value[1])
            if(newPos != False):
                #Creamos el nodo que representa el nuevo estado del agente y lo agregamos al árbol
                #con el estado actual como su padre
                newNode = Node(newPos,currNode)
                solution = self.depthSearchR(l,currL+1,newNode)
                if(solution != False):
                    return solution 

            newPos = self.right(currNode.value[0],currNode.value[1])
            if(newPos != False):
                #Creamos el nodo que representa el nuevo estado del agente y lo agregamos al árbol
                #con el estado actual como su padre
                newNode = Node(newPos,currNode)
                solution = self.depthSearchR(l,currL+1,newNode)
                if(solution != False):
                    return solution
            return False

    #Algoritmo de búsqueda uniforme, misma implementación que bfs pero haciendo uso de una cola con prioridad 
    def uniformSearch(self,showSolution = False):
        #Guardamos las posiciones iniciales para luego imprimirlas
        initX = self.posx
        initY = self.posy
        #En este caso voy a usar las listas nativas de python por una cuestión de legibilidad
        q = []
        #Manejamos tuplas para poder almacenar x e y, ahora también introducimos el peso
        #Para este caso, el peso siempre será 1 por no ser un problema con ponderación
        #Este nodo es parte de la clase Tree, no de LinkedList
        newNode = Node((self.posx,self.posy,1))
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
                #Cada vez que encolamos un nodo, debemos ordenar la lista según el peso de las aristas
                #En este caso es irrelevante pero podría aplicarse a grafos o grillas con ponderación
                #Usando una función lambda extraemos el peso de la arista
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

    #Conjunto de acciones del agente
    def up(self,currX,currY):
        if(currY+1) < self.env.get_sizeY():
            #Verificamos si no se ha explorado ya o es un obstaculo
            if(self.env.floor[currX][currY+1] == 3 or self.env.floor[currX][currY+1] == 1 or self.env.floor[currX][currY+1] == 4):
                return False
            currY += 1
            #Se retorna la posición del siguiente estado y el peso de la arista
            #En este caso el peso de toda arista es 1
            return (currX,currY,1)
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
                return (currX,currY,1)
            else:
                #print("No se puede ir hacia abajo")
                return False
    
    def left(self,currX,currY):
        if(currX-1) >= 0:
            #Verificamos si no se ha explorado ya
            if(self.env.floor[currX-1][currY] == 3 or self.env.floor[currX-1][currY] == 1 or self.env.floor[currX-1][currY] == 4):
                return False
            currX -= 1
            return (currX,currY,1)
        else:
            #print("No se puede ir hacia la izquierda")
            return False

    def right(self,currX,currY):
        if(currX+1) < self.env.get_sizeX():
            #Verificamos si no se ha explorado ya
            if(self.env.floor[currX+1][currY] == 3 or self.env.floor[currX+1][currY] == 1 or self.env.floor[currX+1][currY] == 4):
                return False
            currX += 1
            return (currX,currY,1)
        else:
            #print("No se puede ir hacia la derecha")
            return False


    