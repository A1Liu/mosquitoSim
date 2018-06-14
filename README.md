# Mosquito Population Dynamics

Gene *X* causes:
* Increased likelihood that children are male
* Infertility of female offspring

Simulation Goals:
* [x] Determine formula for phenotype frequencies of next generation
* Determine formula for amount of iterations to kill population given male birthrate *r* and initial infection size *s*.
* Determine variation of mosquito population changes with and without gene *X*

Simulation Roadmap:
* Run 1: Determine a generalized equation to model generation-to-generation changes in the populations
* Run 2: Gain intuition into general pattern of population decay given an initial state
* Run 3: Gain understanding of model behavior with respect to the variation of a single variable
* Run 4: Graphical extension of Run 3
* Run 5: Gain understanding of model behavior with respect to the variation of 1 variable under differing values of 1 variable
* Run 6: Gain understanding of model behavior with respect to the variation of 2 variables simultaneously (3D graphical extension of Run 5)

Hypotheses:
* Generational breeding patterns follow Hardy-Weinberg ratios
* Iterations

Things Learned:
* % male offspring must be above 50% for gene *X* to spread faster than it decays.
* Phenotype frequencies follow Hardy-Weinberg Equations.
* Initial population size affects the eventual iteration count
* Iteration vs Growth seems to be *f*(x) = x^(k) where k < 1
* Iteration vs Initial Population Size seems to be *f*(x) = k^(-x)
* Iteration vs Initial Infection Rate seems to be *f*(x) = a*cot(b*x+c)+k
* Iteration vs Ratio seems to be inverse, *f*(x) = k/x


Sources:
* **[Mosquito Gene Drive](https://www.vox.com/science-and-health/2018/5/31/17344406/crispr-mosquito-malaria-gene-drive-editing-target-africa-regulation-gmo)** - Where I got the idea for the problem from.
* **[Hardy Weinberg Equation](https://www.nature.com/scitable/definition/hardy-weinberg-equation-299)** - The equation I eventually used to model breeding behavior from one generation to the next
* **[Python 3D Plotting](https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html)**
