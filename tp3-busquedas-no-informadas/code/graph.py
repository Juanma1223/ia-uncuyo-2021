class Graph:
    adjMatrix = []

    #El atributo full representa la inicialización de un grafo completo
    def __init__(self, nodeQuantity, full=False):
        #Inicialización de la matriz de adyacencia
        if(full == False):
            self.adjMatrix = [[0 for _ in range(0,nodeQuantity)] for _ in range(0,nodeQuantity)]
        else:
            self.adjMatrix = [[1 for _ in range(0,nodeQuantity)] for _ in range(0,nodeQuantity)]

    def add(self,nodeA,nodeB):
        self.adjMatrix[nodeA][nodeB] = 1
        self.adjMatrix[nodeB][nodeA] = 1

    def disconnect(self,nodeA,nodeB):
        self.adjMatrix[nodeA][nodeB] = 0
        self.adjMatrix[nodeB][nodeA] = 0

    def printGraph(self):
        #Imprimimos un índice de referencia
        print([i for i in range(0,len(self.adjMatrix))])
        print("")
        for node in self.adjMatrix:
            print(node)