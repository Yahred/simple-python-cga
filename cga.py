import random


class Individual:
    def __init__(self, chrom: list[int]) -> None:
        self.chrom = chrom
        self.fitness = None

    def __str__(self) -> str:
        return '{} Fitness: {}'.format(self.chrom, self.fitness)


def initialize_probs(num_genes: int) -> list[float]:
    return [0.5 for _ in range(num_genes)]


def create_individual(probs: list[float]):
    chrom = ['1' if random.uniform(0, 1) < prob else '0' for prob in probs]
    return Individual(''.join(chrom))


def compete(a: Individual, b: Individual, fitness: callable, fitness_min: bool):
    a.fitness = fitness(a.chrom)
    b.fitness = fitness(b.chrom)

    if a.fitness < b.fitness and fitness_min:
        return a, b

    if a.fitness > b.fitness and not fitness_min:
        return a, b

    return b, a


def adjust_probs(probs: list[float], winner: Individual, loser: Individual, generations: int):
    new_probs = []

    for i in range(len(probs)):
        loser_gen = loser.chrom[i]
        winner_gen = winner.chrom[i]

        if winner_gen == loser_gen:
            new_probs.append(probs[i])
            continue

        if winner_gen == '0':
            new_probs.append(probs[i] - 1/generations)
            continue

        new_probs.append(probs[i] + 1/generations)
    return new_probs


def has_converged(probs: list[float], convergence_criteria: float):
    for prob in probs:
        diff = 1 - prob
        if diff > convergence_criteria:
            return False
    return True


def evolve(fitness: callable, num_genes: int, generations: int, convergence_criteria=0.001, fitness_min=False):
    best = None
    probs = initialize_probs(num_genes)

    for _ in range(generations):
        a = create_individual(probs)
        b = create_individual(probs)

        winner, loser = compete(a, b, fitness, fitness_min)

        if not best:
            best = winner
        elif winner.fitness > best.fitness and not fitness_min:
            best = winner
        elif winner.fitness < best.fitness and fitness_min:
            best = winner

        probs = adjust_probs(probs, winner, loser, generations)

        if has_converged(probs, convergence_criteria):
            break

    return best.chrom
