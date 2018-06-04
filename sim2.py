import random as rand
from sim import generation

#Contains method to simulate simple mating patterns

def breed(gen):
    if not isinstance(gen, generation):
        raise TypeError("argument must be a generation")

    clean = gen.population - gen.infected
    infected = gen.infected
    total = gen.population
    totalTemp = total

    newClean = 0
    cross = 0
    newInfected = 0

    while(totalTemp > 1): # Mosquito indices start at 1
        totalsqr = totalTemp*(totalTemp - 1) # Data representing range for random number
        num = rand.randint(1, totalsqr) # Random number representing which mosquitos to breed
        if num <= clean**2: # Neither are infected
            newClean += 2
            clean -= 2
        elif num > totalsqr - infected**2: # both are infected
            infected -= 2
            newInfected += 2
        else: # exactly one is infected
            clean -= 1
            infected -= 1
            cross += 2
        totalTemp -= 2

    return (newClean/total,cross/total,newInfected/total)

    # newTotal = newInfected + cross + newClean
    # return (float(newClean)/newTotal,float(cross)/newTotal,float(newInfected)/newTotal)




# num = rand.randint(1,totalTemp)
# num2 = rand.randint(1, totalTemp - 1)
# if  num > clean:
#     i1 = True
# else:
#     i1 = False
#     clean -= 1
#
# if  num2 > clean:
#     i2 = True
# else:
#     i2 = False
#     clean -= 1
# totalTemp -= 2
# # odd is male
# if i1 != i2:
#     cross += 2
# elif i1 == False:
#     newClean += 2
# else:
#     newInfected += 2
