import time
import matplotlib
import matplotlib.pyplot as plt
from sim import population
import os


# This script simulates multiple run4 attempts, varying 2 attributes instead of 1. I'm gonna try to do them all at once, then build a matrix
# of plots

resultsdir = os.path.join(os.getcwd(),"Results")
resultsdir = os.path.join(resultsdir,"run5")
os.chdir(resultsdir)

#Initial Settings:
popNum = 1000 # As this number increases, so does the detail of each line. Usually not necessary to increase it beyond around 1000
maxIter = 10000 # As a general rule, this number should be over 1000 at all times. If it goes too high, runtime will suffer.

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
# if True:
def getFig(primaryVary, secondaryVary):
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
    plt.clf()
    plt.plot(xlist, ylists[0], label=vary[secondaryVary][0], mfc='r', marker=',')
    plt.plot(xlist, ylists[1], label=vary[secondaryVary][1], mfc='b', marker=',')
    plt.plot(xlist, ylists[2], label=vary[secondaryVary][2], mfc='g', marker=',')
    plt.plot(xlist, ylists[3], label=vary[secondaryVary][3], mfc='y', marker=',')
    plt.plot(xlist, ylists[4], label=vary[secondaryVary][4], mfc='c', marker=',')
    plt.xlabel(labelList[primaryVary])
    plt.ylabel('Iterations Before Extinction')
    plt.title('Iterations vs ' + labelList[primaryVary] + ' with varying ' + labelList[secondaryVary])

    plt.axis([xlist[0], xlist[popNum-1],
    0, 20])# Change these values to make graph prettier

    plt.legend()
    return plt

shortLabelList = ("popSize","init","ratio","growth")
# for primaryVary in range(0,4):
#     for secondaryVary in range(0,4):
#         #This is were the stuff above will go eventually
#         if not primaryVary == secondaryVary:
#             figure = getFig(primaryVary, secondaryVary)
#             title = 'Iter vs ' + shortLabelList[primaryVary] + ' change ' + shortLabelList[secondaryVary]
#             figure.savefig(os.path.join(resultsdir,title)+ ".png", format='png', dpi=1200)
#         # Change Graph


primaryVary = 2
secondaryVary = 3
figure = getFig(primaryVary, secondaryVary)

# figure.show()
title = 'Iter vs ' + shortLabelList[primaryVary] + ' change ' + shortLabelList[secondaryVary]
figure.savefig(os.path.join(resultsdir,title)+ "2.png", format='png', dpi=1200)
