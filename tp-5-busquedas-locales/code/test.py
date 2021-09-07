from environment import Environment

env = Environment(8)
results = []

'''
for i in range(0,100):
    currVal = env.greedyMove()
    if(currVal != False):
        results.append(currVal)
    print("")
    env.printQueens()
'''

for i in range(0,1000):
    currVal = env.annealing_move()
    if(currVal != False):
        results.append(currVal)
    print("")
    env.printQueens()

print("")
env.printQueens()
print(results)