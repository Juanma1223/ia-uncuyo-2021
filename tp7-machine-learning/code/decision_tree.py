import csv
from os import read
from node import Node


# Class in charge of choosing attributes based on acquisition of information
class Tree:

    # Target value to classify
    target = "inclinacion_peligrosa"

    attributes = []

    def __init__(self):
        # Read csv
        file = open(open('arbolado-mza-dataset.csv'))
        reader = csv.reader(file, delimiter=',')
        # Get attributes from csv
        attributes = next(reader)
        # Remove target attribute
        attributes.remove(self.target)

        # Queue where remaining nodes are stored
        q = []
        # Tree's root
        bestAttribute = self.getBestAttrib(attributes, reader)
        root = Node(None,None,reader,attributes,bestAttribute)
        q.append(root)
        q.extend(root.getChildren())

        # Construct decision tree
        while len(q) > 0:
            currNode = q.pop()
            # Calculate best attribute based on acquisition of information
            bestAttribute = self.getBestAttrib(q.remainAttribs, q.rows)
            # Create a new level of the tree
            currNode.createChildren()
            q.extend(currNode.getChildren())


