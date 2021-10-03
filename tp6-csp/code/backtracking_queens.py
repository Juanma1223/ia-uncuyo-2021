from tree import Node

stack = []
queens_num = 12
cantStates = 0

# Si se llega a una  profundidad igual a la cantidad de reinas, devoler el camino hacia ella

# El value del nodo va a ser la columna y el height la fila

# Solo ingresamos en la pila un nodo si este no entra en conflicto con ningún otro

def dfs(queens_num):
    global stack, cantStates
    # Raiz del árbol
    root = Node(13,-1,None)
    stack.append(root)
    while(len(stack) > 0):
        currNode = stack.pop(0)
        cantStates += 1
        # Verificar si llegamos a una solución
        if((currNode.height+1) == queens_num):
            result = currNode.pathToRoot()
            result.pop()
            result.reverse()
            return (result,cantStates)
        # Revisamos las n posiciones de la columna
        for i in range(0,queens_num):
            # Las agregamos a la pila solo en caso de que el check de positivo
            if(check(currNode,i,currNode.height+1) == True):
                # Agregamos el nodo a la pila por recorrer y construimos el árbol
                newNode = Node(i,(currNode.height+1),currNode)
                stack.append(newNode)

    
# Función encargada de revisar si un nodo se puede ingresar o no
def check(currNode,col,height):
    global stack, queens_num
    # Extraemos las posiciones actuales de las reinas
    currPositions = currNode.pathToRoot()
    for i in range(0,len(currPositions)):
        currQueen = currPositions[i]
        # Verificamos que no se encuentre en la misma fila
        if(currQueen[0] == col):
            return False
        # Verificamos que no se encuentre en la misma diagonal
        if(abs(currQueen[0]-col) == abs(currQueen[1]-height)):
            return False
    return True

def printQueens(path):
    tablero = [ [ "*" for _ in range(0,queens_num) ] for _ in range(0,queens_num) ]
    for i in range(0, queens_num):
        currPos = path[i]
        tablero[currPos[0]][currPos[1]] = "o"
    for i in range(0, queens_num):
        for j in range(0, queens_num):
            print(tablero[i][j],end="")

        print("")

result = dfs(queens_num)
#printQueens(result[0])
