from tree import Node
from copy import deepcopy
import time

stack = []
queens_num = 15
cantStates = 0

# Inicializamos los dominios en todas las variables

dom = [ [ i for i in range(0,queens_num) ] for _ in range(0,queens_num) ]


# Generamos una estructura de árbol para representar la solución
def dfs(currNode, currDomains, queens_num):
    currRow = (currNode.height+1)
    # Caso base de la recursión
    if((currNode.height+1) == queens_num):
        result = currNode.pathToRoot()
        result.pop()
        result.reverse()
        return (result,cantStates)
    else:
        # Recorremos todas las opciones del dominio del nodo actual
        for i in range(0,len(currDomains[currRow])):
            # Realizamos una asignación parcial
            newDomains = deepcopy(currDomains)
            newNode = Node(currDomains[currRow][i],currRow,currNode)
            newDomains[currRow] = [currDomains[currRow][i]]
            # Se pasa newDomains por referencia y se le aplica arco-consistencia
            revise(newNode, newDomains)
            if(newDomains == False):
                return None
            result = dfs(newNode,newDomains,queens_num)
            if(result != None):
                return result
    return None


    
# Función encargada de realizar la arco-consistencia para una variable específica
def revise(currNode, newDomains):
    global stack, queens_num, cantStates
    col = currNode.value
    height = currNode.height
    cantStates += 1
    for i in range(0,len(newDomains)):
        domain = newDomains[i]
        # Eliminamos de los dominios la columna de la reina actual
        tam = len(domain)
        j = 0
        while j < (tam):
            # Evitar que se elimine el valor del dominio de la reina actualmente revisada
            currValue = domain[j]
            if(i != height):
                if(currValue == col):
                    domain.remove(col)
                    # Retrocedemos una posición
                    j -= 1
                    tam -= 1
                # Eliminar valores de la diagonal
                elif(abs(currValue-col) == abs(i-height)):
                        domain.remove(currValue)
                        j -= 1
                        tam -= 1
            j = j+1
        if(len(domain) == 0):
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

start = time.time()
root = Node(13,-1,None)
result = dfs(root,dom,queens_num)
end = time.time()
print("Tiempo CSP:",end-start)
printQueens(result[0])
