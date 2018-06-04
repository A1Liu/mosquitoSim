import time
from sim import population,nextGen

#This script simulates a single population slowly decaying due to infection

start = time.process_time()

# Initial population size
popSize = 10000000
# percentage of initial pop. infected
perInfect = .01
# % chance that offspring of an infected male is male
ratio = .6
# Growth of population per generation. Zero means no growth, 1 means double every year, etc.
growth = .01

a = population(popSize,perInfect, ratio, growth) # generation 0
gen = a.getInit()
iter = 0
print(iter, gen.population, gen.infected)
while(gen.population > 1 and gen.infected > 1 and iter < 100000): #a.infected > 0
    gen= nextGen(gen)
    iter += 1
    print(iter, int(gen.population), int(gen.infected))

stop = time.process_time()
print("Time Elapsed:", stop - start)
