import time
import matplotlib
import matplotlib.pyplot as plt
from sim import population


#This script simulates the decay of a set of populations that have varying attributes
# and graphs the results

#Returns the value of one of the attributes
def iterationForm(iteration):
    return .001*iteration

def getPopAttributes(iteration):
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

# Amount of populations to simulate
popNum = 10000
# Max iteration count per population
maxIter = 1000

#list
xlist = []
ylist = []


for x in range(1, popNum):

    pop = population(*getPopAttributes(x))
    xlist.append(iterationForm(x))
    ylist.append(pop.decay(maxIter))

stop = time.process_time()
print("Time Elapsed:", stop - start)

plt.plot(xlist, ylist, 'r.')

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
