# Simple Compact genetic algorithm

This is a simple compact genetic algorithm (SCGA) implementation in Python. 
It is based on the paper [The compact genetic algorithm]
(https://ieeexplore.ieee.org/document/797971) by Harik at. el.

0 external libraries.

This implementation only works for binary codification in the individuals

# Setup

You only need to define a fitness function:

```py
def fitness(individual: list[int]):
    return sum(individual)
```

Define the number of genes in your individuals and the number of generations:

```py
from cga import evolve

best = evolve(fitness, num_genes=10, generations=1000)
```

The evolve function will return the best individual of the evolution process..
