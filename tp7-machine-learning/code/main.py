from decision_tree import Tree
import csv
import copy

f = open("code/tennis.csv")
examples = csv.reader(f)
attributes = next(examples)

def plurality_value(parent_examples):
    return 0

# Return most important attribute and it's values
def importance(attributes,examples):
    return 0

def filterExamples(examples,value):
    return 0


def decision_tree_learning(examples,attributes,parent_examples):
    examples_quant = sum(1 for _ in examples)
    if(examples_quant == 0):
            return plurality_value(parent_examples)
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
            exs = filterExamples(examples,value)
            subtree = decision_tree_learning(exs, remainingAttributes, examples)
            newTree.addBranch(subtree,value)
        return newTree



dt = Tree(examples, attributes, examples)

f.close()