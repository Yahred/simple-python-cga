# Simple Compact genetic algorithm

This is a simple compact genetic algorithm (SCGA) implementation in Python. 
It is based on the paper [A Simple Compact Genetic Algorithm for Multiobjective Optimization]
(https://ieeexplore.ieee.org/document/1004388) by Kalyanmoy Deb and Debayan Deb.

0 external libraries.

This implementation only works for binary codification in the individuals

# Setup

You only need to define a fitness function:

```
def fitness(a: list[int]):
    return sum(a)
```

Define the number of genes in your individuals and the number of generations:

```
from simple-python-cga import evolve

best = evolve(fitness, num_genes=10, generations=1000)
```

The function evolve will return the best individual of the evolution process.
