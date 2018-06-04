import time
from sim import generation
from sim2 import breed

# The script simulates the mating patterns of a single generation
# for a specific amount of times, and prints the average result.

start = time.process_time()

popinit = 100000
infectinit = 1000
cleaninit = popinit-infectinit
a = generation(popinit,infectinit)
hin = (infectinit/popinit)**2
hcross = 2*(infectinit/popinit)*(cleaninit/popinit)
hclean = (cleaninit/popinit)**2
iter = 0
out = None
cross = 0.0
clean = 0.0
infect = 0.0

while(iter < 10000): #a.infected > 0
    iter+=1
    out = breed(a)
    clean += out[0]
    cross += out[1]
    infect += out[2]
    print(clean/iter-hclean,cross/iter-hcross,infect/iter-hin) # Does it approximate hardy-weinberg?


stop = time.process_time()
print((a.population - a.infected)/a.population, a.infected/a.population)
print(clean/iter,cross/iter,infect/iter)
print("Time Elapsed:", stop - start)
