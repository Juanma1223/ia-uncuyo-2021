from random import randint

#Clase que representa el entorno en el que se mueve la aspiradora
class Environment:
    floor = [[]]
    __sizeX = 0
    __sizeY = 0

    #Inicializamos el entorno con suciedad aleatoria y fijamos el tamaño
    def __init__(self,sizeX,sizeY,dirt_rate):
        #Inicializacion de la lista por comprension
        self.floor = [ [ 0 for _ in range(sizeX) ] for _ in range(sizeY) ]
        for i in range(0,sizeX):
            for j in range(0,sizeY):
                is_dirty = randint(1,10)
                if(is_dirty <= dirt_rate*10):
                    self.floor[i][j] = 1
        self.__sizeX = sizeX
        self.__sizeY = sizeY

    def get_sizeX(self):
        return self.__sizeX

    def get_sizeY(self):
        return self.__sizeY

    def set_clean(self,x,y):
        try:
            self.floor[x][y] = 0
        except:
            print("",end="")

    def is_dirty(self,x,y):
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
            print(self.floor[i])
            print("")
	#def accept_action(self,action):
    def get_performance(self): 
        counter = 0
        #Contamos la cantidad de 1s y los dividimos por el tamaño de x multiplicado por el de y
        for i in range(0, self.__sizeX):
            for j in range(0, self.__sizeY):
                if(self.floor[i][j] == 1):
                    counter += 1
        return "Porcentaje de suciedad en el entorno: " + str(counter / (self.__sizeX*self.__sizeY) * 100) + "%"