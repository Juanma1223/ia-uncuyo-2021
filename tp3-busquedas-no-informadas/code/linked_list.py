class Node:
    value = None
    nextNode = None
    prevNode = None

    def __init__(self,value):
        self.value = value

class LinkedList:
    head = None
    #Falta implementar
    last = None

    def __init__(self):
        self.head = None
    
    def add(self,value):
        newNode = Node(value)
        if(self.head == None):
            self.head = newNode
            self.last = newNode
        else:
            self.head.prevNode = newNode
            newNode.nextNode = self.head
            newNode.prevNode = None
            self.head = newNode
    
    def printList(self):
        currNode = self.head
        print("[" , end = ' ')
        while currNode != None:
            print(currNode.value,end = '')
            print(" ",end = '')
            currNode = currNode.nextNode
        print("]")

    def pop(self):
        retVal = self.head.value
        if(self.last == self.head):
            self.head = None
            self.head = None
            return retVal
        self.head = self.head.nextNode
        self.head.prevNode = None
        return retVal

    def dequeue(self):
        retVal = self.last.value
        #Caso en el cual solo hay un nodo
        if(self.last == self.head):
            self.head = None
            self.head = None
            return retVal
        self.last = self.last.prevNode
        self.last.nextNode = None
        return retVal
        


