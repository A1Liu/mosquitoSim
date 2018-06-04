# Mosquito Population Dynamics

Gene *X* causes:
* Increased likelihood that children are male
* Infertility of female offspring

Simulation goals:
* [x] Determine formula for phenotype frequencies of next generation
* Determine formula for amount of iterations to kill population given male birthrate *r* and initial infection size *s*.
* Determine variation of mosquito population changes with and without gene *X*

Things Learned:
* % male offspring must be above 50% for gene *X* to spread faster than it decays.
* Phenotype frequencies follow Hardy-Weinberg Equations.
* Initial population size affects the eventual iteration count
  * Hypothesis: relationship is logarithmic

Sources:
* **[Mosquito Gene Drive](https://www.vox.com/science-and-health/2018/5/31/17344406/crispr-mosquito-malaria-gene-drive-editing-target-africa-regulation-gmo)** - Where I got the idea for the problem from.
* **[Hardy Weinberg Equation](https://www.nature.com/scitable/definition/hardy-weinberg-equation-299)** - The equation I eventually used to model breeding behavior from one generation to the next
