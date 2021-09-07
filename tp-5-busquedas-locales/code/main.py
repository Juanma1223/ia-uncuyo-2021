from environment import Environment

env = Environment(4)

for i in range(0,1000):
    env.greedyMove()
    print("")
    env.printQueens()
print("")
env.printQueens()