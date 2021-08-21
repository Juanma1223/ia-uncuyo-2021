from linked_list import LinkedList

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

    def breadth_search(self):
        found = False
        #Lista enlazada que funcionará como queue para lugares por visitar
        q = LinkedList()
        #Manejamos tuplas para poder almacenar x e y
        q.add((self.posx,self.posy))
        #Agregamos la posición inicial a los nodos explorados con un 3
        self.env.floor[self.posx][self.posy] = 3
        while q.head != None:            
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

            currPos = q.dequeue()
            self.posx = currPos[0]
            self.posy = currPos[1]
            #Verificamos si alcanzamos el objetivo
            if(self.env.floor[self.posx][self.posy] == 2):
                found = True
                break
            #Marcamos esta posición como explorada
            self.env.floor[self.posx][self.posy] = 3
        
        return found



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


    