from environment import Environment

env = Environment(8,200)

solutions = []

#for j in range(0,30):
#for i in range(0,30):
while True:
    env.newGeneration()
    #print("")
    #env.printPopulation()
    sol = env.getBestSolution()
    print(sol.getFitness())
    if(sol.getFitness() >= 56):
        sol.printQueens()
        break