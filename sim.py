import random

#Contains resources necessary for simulating basic changes generation to generation
#and in populations over time

class generation:

    def __init__(self, population, infected, ratio = .5, growth = 0):
        self.population = population
        self.infected = infected
        self.ratio = ratio
        self.growth = growth

class population:

    def __init__(self, popSize, perInfect, ratio, growth):
        self.popSize = popSize
        self.perInfect = perInfect
        self.ratio = ratio
        self.growth = growth

    def decay(self, maxIter = 1000):
        gen = generation(self.popSize,self.perInfect*self.popSize,self.ratio,self.growth)
        iter = 0
        while(gen.population > 1 and gen.infected > 1 and iter < maxIter): #a.infected > 0
            gen = nextGen(gen)
            iter += 1
        return iter

    def getInit(self):
        return generation(self.popSize,self.perInfect*self.popSize,self.ratio,self.growth)

#Math based
def nextGen(gen):
    total = gen.population*(gen.growth+1)
    clean = (gen.population - gen.infected)/gen.population
    infected = gen.infected/gen.population
    newInfect = gen.ratio*2*clean*infected*total # New infected count.
    newPop = newInfect + total*clean**2 #New Population size
    return generation(newPop, newInfect,gen.ratio, gen.growth) #TODO: cast to integer?

#Simulation based
def nextGen1(gen):#TODO: improve runtime

    clean = gen.population - gen.infected
    infected = gen.infected
    total = gen.population
    if (total % 2 == 1):
        clean+=1
        total+=1
    newClean = 0
    newInfected = 0
    growth = 2.00
    # survival = 5

    while(total > 0):#Randomness is computationally expensive
        #It's usually cheaper to call random once, then split that randomness into multiple parts
        first = random.randint(1,total)
        firstInfected = False
        if first > clean:
            firstInfected = True
        else:
            clean-=1
        total-=1
        second = random.randint(1,total)
        secondInfected = False
        if second > clean:
            secondInfected = True
        else:
            clean-=1
        total-=1

        # if (random.randint(1,survival) == 1):
        #     if (firstInfected or secondInfected) and not (firstInfected and secondInfected):
        #         if (random.randint(1,3) > 1):
        #             newInfected += survival*growth
        #     elif not firstInfected:
        #         newClean += survival*growth


        if (firstInfected or secondInfected) and not (firstInfected and secondInfected):
            if (random.randint(1,9) > 4):
                newInfected += growth
        elif not firstInfected:
            newClean += growth

    return generation(int(newClean + newInfected),int(newInfected))




# a = generation(100000,0)
# iter = 0
# print iter,"  ",a.population,"  ",a.infected
# while(a.population > 0 and a.infected > -1 and iter < 100): #a.infected > 0
#     iter+=1
#     a = nextGen1(a)
#     print iter,"  ",a.population,"  ",a.infected
