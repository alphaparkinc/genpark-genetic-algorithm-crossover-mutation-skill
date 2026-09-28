"""Genetic Algorithm Optimization Engine
100% Python Standard Library (random).
"""

import random

class GeneticAlgorithmOptimizer:
    """Evolutionary binary search and global optimization."""
    def __init__(self, gene_length=16, pop_size=30, mutation_rate=0.05, elitism=2):
        self.gene_length = gene_length
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.elitism = elitism

    def optimize(self, fitness_fn, generations=50):
        pop = [[random.choice([0, 1]) for _ in range(self.gene_length)] for _ in range(self.pop_size)]

        for g in range(generations):
            scores = [(fitness_fn(ind), ind) for ind in pop]
            scores.sort(key=lambda x: x[0], reverse=True)

            new_pop = [scores[i][1] for i in range(self.elitism)]
            while len(new_pop) < self.pop_size:
                p1 = max(random.sample(scores, 3), key=lambda x: x[0])[1]
                p2 = max(random.sample(scores, 3), key=lambda x: x[0])[1]
                cut = random.randint(1, self.gene_length - 1)
                child = p1[:cut] + p2[cut:]
                child = [1 - bit if random.random() < self.mutation_rate else bit for bit in child]
                new_pop.append(child)
            pop = new_pop

        best_score, best_ind = max((fitness_fn(ind), ind) for ind in pop)
        return {
            "best_fitness": best_score,
            "best_individual": best_ind,
            "generations_run": generations
        }
