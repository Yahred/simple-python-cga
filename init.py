from cga import evolve

def fitness(bin: str):
    ind = int(bin, 2)
    return ind


best = evolve(fitness, num_genes=10, generations=10000, fitness_min=True)

print(best)