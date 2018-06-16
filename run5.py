import time
import matplotlib
import matplotlib.pyplot as plt
from sim import population
import os


# This script simulates multiple run4 attempts, varying 2 attributes instead of 1. I'm gonna try to do them all at once, then build a matrix
# of plots

# resultsdir = os.path.join(os.getcwd(),"Results")
# resultsdir = os.path.join(resultsdir,"run5")
# os.chdir(resultsdir)

#Initial Settings:
popNum = 1000
maxIter = 10000

#

# Bounds of graphs' x axis: Popsize, init, ratio, growth
xupper = [100000,1,1,5]
xlower = [100,0,.5,-.2]

#Values for graphs
vary = (
(100,1000,10000,50000,100000), # Population Size
(0,.05,.1,.5,1), # Initial Infection Rate
(.5,.625,.75,.875,1), # Ratio
(-.2,-.1,0,2,5) # Growth
)

# Default values
varydef = (10000, .5, .75, 0)
baseXList = range(0,popNum) # Base list for x values
labelList = ("Population Size","Initial Infection Rate","Ratio","Growth Rate")
primaryVary = 3
secondaryVary = 2

if not secondaryVary == primaryVary:
    ylists = []
    xlist = [x/1000*(xupper[primaryVary]-xlower[primaryVary])+xlower[primaryVary] for x in baseXList]
    for mitNum in range(0,5):
        iteration = [*varydef]
        iteration[secondaryVary] = vary[secondaryVary][mitNum]
        ylist = []
        for itNum in xlist:
            iteration[primaryVary] = itNum
            ylist.append(population(*iteration).decay(maxIter))
        ylists.append(ylist)
            # Change point

        # Change line
    plt.plot(xlist, ylists[0], label=vary[secondaryVary][0], mfc='r', marker=',')
    plt.plot(xlist, ylists[1], label=vary[secondaryVary][1], mfc='b', marker=',')
    plt.plot(xlist, ylists[2], label=vary[secondaryVary][2], mfc='g', marker=',')
    plt.plot(xlist, ylists[3], label=vary[secondaryVary][3], mfc='y', marker=',')
    plt.plot(xlist, ylists[4], label=vary[secondaryVary][4], mfc='c', marker=',')
    plt.xlabel(labelList[primaryVary])
    plt.ylabel('Iterations Before Extinction')
    plt.title('Iterations vs ' + labelList[primaryVary] + ' with varying ' + labelList[secondaryVary])
    plt.legend()
    print(xlist[popNum-1])
    plt.axis([xlist[0], xlist[popNum-1], 0, 100])

    plt.show()
    # Plot here
    # Save here
    # Plot and save

for primaryVary in range(0,3):
    for secondaryVary in range(0,3):
        #This is were the stuff above will go eventually
        pass
        # Change Graph




# 1000 points
growth = (0,10) # Standard is: 0 Graphs at: -5, -2, 0, 2, 5
initInf = (0,1) # Standard is: .5 Graphs at 0, .25, .5, .75, 1
popSize = (100,100000) # Standard is: 10,000 Graphs at: 100, 1000, 10000, 50000, 100000
ratio = (.5,1) # Standard is: .75 Graphs at: .5, .625, .75, .875, 1

# Markers: color letter + ',' -- comma means pixel
