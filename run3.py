import time
import matplotlib
from sim import population

#This script simulates the decay of a set of populations that have varying attributes

def getPopAttributes(iteration):
    #Determine population attributes based on iteration number

    # Initial population size
    popSize = 10000
    # percentage of initial pop. infected
    perInfect = .5
    # % chance that offspring of an infected male is male
    ratio = .5
    # Growth of population per generation. 0 means no growth, 1 means double every year, etc.
    growth = 6

    return (popSize, perInfect, ratio, growth)

start = time.process_time()

# Amount of populations to simulate
popNum = 1000
# Max iteration count
maxIter = 10000

for x in range(1, popNum):
    pop = population(*getPopAttributes(x))
    print(x,pop.decay(maxIter))

stop = time.process_time()
print("Time Elapsed:", stop - start)
