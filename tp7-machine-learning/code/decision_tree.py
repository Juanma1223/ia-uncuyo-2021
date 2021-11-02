class Tree:
    subtrees = []
    attribute = ""
    label = ""
    # attributes = []


class Tree:

    def __init__(self,attribute):
        self.label = attribute


    def addBranch(self,tree,label):
        self.subtrees.append(tree)
        self.label = label