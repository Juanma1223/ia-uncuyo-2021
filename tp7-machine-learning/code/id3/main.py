from decision_tree import Tree
import csv
import copy
import math

f = open("code/tennis.csv")
examples = csv.reader(f)
attributes = next(examples)

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


def valueProbability(attribute,value):
    return 0

# Return most important attribute and it's values
def importance(attributes,examples):
    for attribute in attributes:
        values = getValues(attribute,examples)
        entropy = 0
        # Calculate entropy
        for value in values:
            prob = valueProbability(attribute,value)
            entropy = entropy + (prob*math.log(1/prob,2))


# Filter rows where attribute == value
def filterExamples(examples,attribute,value):
    global attributes
    filteredExamples = []
    attributeIndex = attributes.index(attribute)
    for example in examples:
        if(example[attributeIndex] == value):
            filteredExamples.append(example)
    return filteredExamples


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
        return "yes"
    elif(counter == 0):
        return "no"
    else:
        attribute = importance(attributes,examples)
        newTree = Tree(attribute)
        remainingAttributes = copy(attributes)
        remainingAttributes.remove(attribute)
        for value in attribute.values:
            # Filter examples and return only those with value vk
            exs = filterExamples(examples,attribute,value)
            subtree = decision_tree_learning(exs, remainingAttributes, examples)
            newTree.addBranch(subtree,value)
        return newTree

#dt = Tree(examples, attributes, examples)

f.close()
