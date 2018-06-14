import time
import matplotlib
import matplotlib.pyplot as plt
from sim import population


#This script simulates multiple run4 attempts, varying 2 attributes instead of 1. I'm gonna try to do them all at once, then build a matrix
# of plots

# Returns the value of the meta-attribute
def miterForm(miter):
    return

#Returns the value of one of the attributes
def iterationForm(iteration):
    return .001*iteration

def getPopAttributes(iteration, miter):
    #Determine population attributes based on iteration number

    # Initial population size 10000
    popSize = 10000

    # percentage of initial pop. infected
    perInfect = .01

    # % chance that offspring of an infected male is male .6
    ratio = .6
    # Growth of population per generation. 0 means no growth, 1 means double every year, etc.
    growth = iterationForm(iteration)

    return (popSize, perInfect, ratio, growth)

start = time.process_time()

# Amount of graphs to make
graphNum = 5
# Amount of populations to simulate
popNum = 10000
# Max iteration count per population
maxIter = 1000

#list
xlist = []
totalList = []
firstRun = True

for x in range(1, graphNum):
    ylist = []
    for y in range(1, popNum):
        pop = population(*getPopAttributes(y,x))
        if (firstRun):
            xlist.append(iterationForm(y))
        ylist.append(pop.decay(maxIter))

    totalList.append(xlist)
    totalList.append(ylist)
    firstRun = False

stop = time.process_time()
print("Time Elapsed:", stop - start)

plt.plot(**totalList)

xmin = iterationForm(0)
xmax = iterationForm(popNum)
ymin = 0
ymax = 75

plt.axis([xmin, xmax, ymin, ymax])
plt.xlabel('Population Growth Rate')
plt.ylabel('Iterations Before Extinction')
plt.title('Iterations vs Growth Rate')
s = "Growth Rate = 0, Pop Size = 10000, Initial = 1%, Ratio = .6"
s = "Pop Size = 10000, Initial = 1%, Ratio = .6"
plt.text(2, ymax/2, s)

plt.show()
