# This class is in charge of assembling every subtree that's created once a variable is chosen
class Node:

    parent = None
    children = []
    # Value chosen to take this path
    value = ""
    # Holds data rows corresponding to the current attribute
    rows = None
    # If this node is a leave, classify with corresponding output value    
    classify = None
    # Possible values for this attribute
    values = []
    # Remaining attributes
    remainAttribs = None
    # Next attribute that decides the path
    nextAttrib = None


    def __init__(self,parent,value,rows,remainAttribs,nextAttrib):
        self.parent = parent
        self.value = value
        self.rows = self.filterRows(rows)
        # Remove current attribute from attributes
        remainAttribs.pop(parent.nextAttrib)
        self.remainAttribs = remainAttribs
        self.nextAttrib = nextAttrib
        self.values = self.findValues()


    # Returns all children
    def getChildren(self):
        return self.children

    # Returns child with a certain value to follow the path
    def getChild(self,value):
        return 0

    
    # Get parent's rows and filter them
    def filterRows(self,rows):
        filteredRows = []
        for row in rows:
            if(row[self.parent.nextAttrib] == self.value):
                filteredRows.append(row)
        self.rows = filteredRows


    def findValues(self):
        # Gather every single value for current attribute
        values = []
        for row in self.rows:
            # Ask if a value is already present in the list
            currValue = row[self.nextAttrib]
            if(values.count(currValue) == 0):
                values.append(currValue)
        return values

    # Create children nodes with every available value for current attribute
    def createChildren(self):
        for value in self.values:
            Node(self,value,self.rows,self.remainAttribs,None)
