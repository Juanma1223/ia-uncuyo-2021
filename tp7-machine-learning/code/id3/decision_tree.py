class Tree:

    def __init__(self,attribute):
        self.attribute = attribute
        self.level = 0
        self.label = ""
        self.subtrees = []


    def addBranch(self,tree,label,parent):
        self.subtrees.append(tree)
        tree.label = label
        self.parent = parent
        self.level = parent.level + 1

    def getChildren(self):
        return self.subtrees

    def printTree(self):
        q = []
        q.append(self)
        while len(q) != 0:
            currentNode = q.pop(0)
            print("Decision:",currentNode.label)
            print(currentNode.attribute)
            print("lvl",currentNode.level)
            print("")
            children = currentNode.getChildren()
            q.extend(children)