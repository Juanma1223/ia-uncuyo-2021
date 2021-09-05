from environment import Environment

env = Environment()

while(env.greedyMove()):
    print("")
    env.printQueens()
print("")
env.printQueens()