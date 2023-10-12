from cga import evolve

def fitness(a: list[int]):
    return sum(a)

best = evolve(fitness, num_genes=10, generations=5000)

print(best)