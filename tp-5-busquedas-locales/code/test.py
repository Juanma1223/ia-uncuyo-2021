from environment import Environment

env = Environment(8)
results = []

'''
for i in range(0,100):
    currVal = env.greedyMove()
    results.append(currVal)
    print("")
    env.printQueens()

'''
for i in range(0,500):
    currVal = env.annealing_move()
    results.append(currVal)
    print("")
    env.printQueens()
print("")
env.printQueens()
print(results)