from decision_tree import Tree
import csv
import copy
import math

def plurality_value(examples):
    noCount = 0
    yesCount = 0
    for example in examples:
        if(example[4] == "yes"):
            yesCount = yesCount + 1
        else:
            noCount = noCount + 1
    if(noCount >= yesCount):
        return "no"
    else:
        return "yes"


# Filter rows where attribute == value
def filterExamples(examples,attribute,value):
    global attributes
    filteredExamples = []
    attributeIndex = attributes.index(attribute)
    for example in examples:
        if(example[attributeIndex] == value):
            filteredExamples.append(example)
    return filteredExamples

# Return all posible values for an attribute
def getValues(attribute,examples):
    global attributes
    values = []
    attributeIndex = attributes.index(attribute)
    for example in examples:
        currentValue = example[attributeIndex]
        # Check if it's not in array yet
        if(values.count(currentValue) == 0):
            values.append(currentValue)
    return values

def booleanProb(q):
    print(q)
    return -(q*math.log(q,2)+(1-q)*math.log(1-q,2))

def getPositivesNegatives(examples,attribute,value):
    positives = 0
    negatives = 0
    filtered = examples
    if(value != ""):
        filtered = filterExamples(examples,attribute,value)
    for example in filtered:
        if(example[4] == "yes"):
            positives = positives + 1
        else:
            negatives = negatives + 1
    return (positives,negatives)

def remainder(attribute,examples):
    values = getValues(attribute,examples)
    remainder = 0
    examplesQuantity = sum(1 for _ in examples)
    for value in values:
        valuePN = getPositivesNegatives(examples,attribute,value)
        term1 = (valuePN[0]+valuePN[1])/examplesQuantity
        term2 = booleanProb(valuePN[0]/(valuePN[0]+valuePN[1]))
        remainder = remainder + term1*term2
    return remainder

# Return most important attribute and it's values
def importance(attributes,examples):
    maxInfoGain = 0
    bestAttribute = ""
    for attribute in attributes:
        # Calculate infoGain
        attributePN = getPositivesNegatives(examples,attribute,"")
        attributeEntropy = booleanProb(attributePN[0]/(attributePN[0]+attributePN[1]))
        rem = remainder(attribute,examples)
        infoGain = attributeEntropy - rem
        if(infoGain > maxInfoGain):
            maxInfoGain = infoGain
            bestAttribute = attribute
    return bestAttribute


def decision_tree_learning(examples,attributes,parent_examples):
    examples_quant = sum(1 for _ in examples)
    if(examples_quant == 0):
        return plurality_value(parent_examples)
    elif(len(attributes) == 0):
        return plurality_value(examples)
    counter = 0
    for example in examples:
        if(example[4] == "yes"):
            counter = counter + 1
    if(counter == examples_quant):
        leaf = Tree("yes")
        return leaf
    elif(counter == 0):
        leaf = Tree("no")
        return leaf
    else:
        attribute = importance(attributes,examples)
        newTree = Tree(attribute)
        remainingAttributes = copy(attributes)
        remainingAttributes.remove(attribute)
        values = getValues(attribute,examples)
        for value in values:
            # Filter examples and return only those with value vk
            exs = filterExamples(examples,attribute,value)
            subtree = decision_tree_learning(exs, remainingAttributes, examples)
            newTree.addBranch(subtree,value)
        return newTree

f = open("code/id3/tennis.csv")
reader = csv.reader(f)
attributes = next(reader)
examples = []
for row in reader:
    examples.append(row)
dt = decision_tree_learning(examples, attributes, examples)
dt.printTree()

f.close()
