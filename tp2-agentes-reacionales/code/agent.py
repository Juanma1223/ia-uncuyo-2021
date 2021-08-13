from random import randint

class Agent:
    currLife = 0
    totalLife = 0
    currCleaned = 0
    def __init__(self,env,totalLife):
        #Inicializamos el entorno donde se encuentra el agente
        self.__env = env
        #Inicializamos la cantidad de acciones en 1000
        self.currLife = totalLife
        self.totalLife = totalLife
        #Inicializamos la posicion de manera aleatoria
        self.__currX = randint(0, env.get_sizeX())
        self.__currY = randint(0, env.get_sizeY())

    def perspective(self): #sensa el entorno
        floorSituation = self.__env.is_dirty(self.__currX,self.__currY)
        if(floorSituation == 1):
            self.clean()
            #Usamos una accion
        else:
            self.idle()

    def clean(self):
        # Limpia
        self.__env.set_clean(self.__currX,self.__currY)
        self.currCleaned += 1

    def up(self):
        try:
            self.__currY += 1
        except:
            print("",end="")

    def down(self):
        try:
            self.__currY -= 1
        except:
            print("",end="")

    def left(self):
        try:
            self.__currX -= 1
        except:
            print("",end="")

    def right(self):
        try:
            self.__currX += 1
        except:
            print("",end="")

    def idle(self):
        print("",end="") # no hace nada

    def get_performance(self):
        return "Cuadriculas limpiadas: " + str(self.currCleaned)
    
    def think(self): # implementa las acciones a seguir por el agente
        #Sensa el ambiente
        self.perspective()
        #Se mueve aleatoriamente en alguna direccion
        direction = randint(0,3)
        if(direction == 0):
            self.up()
        elif(direction == 1):
            self.right()
        elif(direction == 2):
            self.down()
        else:
            self.left()
        self.currLife -= 1
        