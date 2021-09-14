# Clase que representa al entorno donde se desarrollan los individuos

from random import randint
from random import random
from individual import Individual
from queen import Queen

class Environment:

    # Población actual
    population = []
    # Cantidad de individuos que mantenemos en la población
    populationLen = 10
    # Cantidad de reinas
    queensQuan = 8
    # Cantidad de individuos a agregar de la generación anterior
    prevGeneration = 5

    def __init__(self,queens = 8, populationLen = 10):
        self.populationLen = populationLen
        # Mantenemos un 20% de la generación actual
        prevGeneration = round(populationLen/5)
        self.queenQuan = queens
        # Creación de la primera generación
        for _ in range(0,self.populationLen):
            newIndividual = Individual(self.queensQuan)
            self.population.append(newIndividual)
        

    def newGeneration(self):
        newGeneration = []
        children = []
        for _ in range(0,round(self.populationLen)):
            # Elección de dos padres
            x = self.randomSelection()
            y = self.randomSelection(x)
            # Generamos 2 hijos
            newChildren = self.crossover1(x,y)
            self.mutation(newChildren[0])
            self.mutation(newChildren[1])
            children.extend(newChildren)
        # Mezclamos la nueva generación con la actual
        self.population.sort(reverse = True,key = lambda x : x.getFitness())
        for i in range(0,self.prevGeneration):
            children.insert(0,self.population[i])
        children.sort(reverse = True,key = lambda x : x.getFitness())
        #print("Insertar en la newGeneration solo los *populationLen* mejores")
        i = 0
        while i < self.populationLen:
            newGeneration.append(children[i])
            i += 1
        # newGeneration[0].printQueens()
        #print(newGeneration[0].getFitness())
        self.population = newGeneration
        
    '''
    # Elección de un individuo para reproducirse según la función de fitness
    def randomSelection(self,x = None):
        num = randint(0,self.populationLen-1)
        chosen = self.population[num]
        # Verificar que no sea el mismo padre
        if(x != None and chosen == x):
            return self.randomSelection(x)      
        prob = random()
        # Seleccionar el mayor de los valores de fitness de la población
        maxFitness = 0
        #maxFitness = self.maxFitness()
        for individual in self.population:
            maxFitness += individual.getFitness()
        fitProb = (chosen.getFitness())/maxFitness
        # La probabilidad será chosenFitness/maxFitness
        if(prob < fitProb):
            return chosen
        else:
            return self.randomSelection()

    '''

    # Elección de un individuo para reproducirse según la función de fitness
    def randomSelection(self,x = None):
        i = 0
        maxFitness = 0
        #maxFitness = self.maxFitness()
        for individual in self.population:
            maxFitness += individual.getFitness()
        while True:
            # Comenzamos de nuevo
            if(i == self.populationLen):
                i = 0
            # Elegimos candidato
            chosen = self.population[i]
            # Verificar que no sea el mismo padre
            if(x != None and chosen == x):
                i = i+1
                continue     
            prob = random()
            # Seleccionar el mayor de los valores de fitness de la población
            fitProb = (chosen.getFitness())/maxFitness
            # La probabilidad será chosenFitness/maxFitness
            if(prob < fitProb):
                return chosen
            i = i+1

    def maxFitness(self):
        maximum = 0
        for individual in self.population:
            currFitness = individual.getFitness()
            if(currFitness > maximum):
                maximum = currFitness
        return maximum

    # Simple operador de cruzamiento de un corte
    def crossover1(self,ind1,ind2):
        ind1Queens = ind1.getQueens()
        ind2Queens = ind2.getQueens()
        # Descendencia
        child1 = Individual(self.queensQuan)
        child2 = Individual(self.queensQuan)
        child1.queens = []
        child2.queens = []
        # Cantidad de reinas
        queensQuan = len(ind1Queens)
        # Elegimos el punto de corte
        num = randint(0,queensQuan-1)
        # Construimos el primer hijo
        for i in range(0,queensQuan):
            if(i < num):
               child1.queens.append(ind1Queens[i])
               child2.queens.append(ind2Queens[i])
            else:
                child1.queens.append(ind2Queens[i]) 
                child2.queens.append(ind1Queens[i]) 
        '''
         print("Padre 1")
        ind1.printQueens()
        print("Padre 2")
        ind2.printQueens()
        print("Hijo 1")
        child1.printQueens()
        print("Hijo 2")
        child2.printQueens()
        '''
        return (child1,child2)


    # Operador de cruzamiento en 2 puntos
    def crossover2(self,ind1,ind2):
        ind1Queens = ind1.getQueens()
        ind2Queens = ind2.getQueens()
        # Descendencia
        child1 = Individual(self.queensQuan)
        child2 = Individual(self.queensQuan)
        child1.queens = []
        child2.queens = []
        # Cantidad de reinas
        queensQuan = len(ind1Queens)
        # Elegimos el punto de corte
        num1 = randint(0,queensQuan-1)
        num2 = randint(0,queensQuan-1)
        # Evitamos seleccionar el mismo número
        while(num2 == num1):
            num2 = randint(0,queensQuan-1)
        for i in range(0,queensQuan):
            if(i < num1):
               child1.queens.append(ind1Queens[i])
               child2.queens.append(ind2Queens[i])
            elif(i > num1 and i < num2):
                child1.queens.append(ind2Queens[i])
                child2.queens.append(ind1Queens[i])
            else:
                child1.queens.append(ind1Queens[i]) 
                child2.queens.append(ind2Queens[i])
        return (child1,child2)

    def mutation(self,individual):
        prob = 0.005
        # Elegir reina al azar
        queens = individual.getQueens()
        queen = queens[randint(0,len(queens)-1)]
        # Posición aleatoria
        pos = (queen.getPosition()[0],randint(0,len(queens)-1))
        # Número aleatorio
        randnum = random()
        if(randnum <= prob):
            print("Mutación")
            queen.move(pos)
        return individual

    def getPopulation(self):
        return self.population

    def printPopulation(self):
        for individual in self.population:
            individual.printQueens()
            print("")
    
    def getBestSolution(self):
        maximum = 0
        bestInd = None
        for ind in self.population:
            if(ind.getFitness() > maximum):
                maximum = ind.getFitness()
                bestInd = ind
        return bestInd
    