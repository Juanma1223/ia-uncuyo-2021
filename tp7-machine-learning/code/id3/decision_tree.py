class Tree:
    subtrees = []
    attribute = ""
    label = ""
    # attributes = []

    def __init__(self,attribute):
        self.label = attribute


    def addBranch(self,tree,label):
        self.subtrees.append(tree)
        self.label = label

    def printTree(self):
        q = []
        q.extend(self.subtrees)
        while len(q) != 0:
            currentNode = q.pop()
            print(currentNode.label)
            q.extend(currentNode.subtrees)