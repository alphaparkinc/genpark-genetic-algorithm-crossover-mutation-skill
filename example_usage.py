from client import GeneticAlgorithmOptimizer

def main():
    ga = GeneticAlgorithmOptimizer(gene_length=12, pop_size=20)
    res = ga.optimize(lambda ind: sum(ind), generations=25)
    print("Genetic Algorithm Verification:")
    print(f"Generations: {res['generations_run']}")
    print(f"Best Fitness: {res['best_fitness']}/{ga.gene_length}")
    print(f"Optimal Individual: {res['best_individual']}")

if __name__ == "__main__":
    main()
