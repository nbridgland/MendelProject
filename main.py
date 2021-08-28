import numpy as np


# [1,1] -> homozygous dominant
# [0,0] -> homozygous recessive
# [1.0] -> heterozygous
# From pool of parents, pick 2
# Given any 2 parents, determine offspring

def generate_offspring(parent_1_genotype, parent_2_genotype, n_offspring):
    offspring_dictionary = {'T T': 0, 't t': 0, 'T t': 0}
    for k in range(n_offspring):
        offspring_gene_1 = np.random.choice(parent_1_genotype.split(' '))
        offspring_gene_2 = np.random.choice(parent_2_genotype.split(' '))
        if offspring_gene_1 != offspring_gene_2:
            offspring_dictionary['T t'] += 1
        else:
            if offspring_gene_1 == 'T':
                offspring_dictionary['T T'] += 1
            if offspring_gene_1 == 't':
                offspring_dictionary['t t'] += 1
    return offspring_dictionary


def garden_simulation(start_pop: dict, n_generations: int, n_crosses, max_pop_size: int):
    # Find relative weighting of each parents group in starting population
    # Find probable offspring of each set of parents, including self-cross
    # Sum up
    total_pop = sum(list(start_pop.values()))
    current_pop = start_pop
    counter = 0
    while counter < n_generations:
        total_pop = sum(list(current_pop.values()))
        weights = [count / total_pop for count in current_pop.values()]
        next_pop = dict()
        for j in range(n_crosses):
            parents = np.random.choice(list(current_pop.keys()), size=2, p=weights)
            offspring = generate_offspring(parents[0], parents[1], int(max_pop_size / n_crosses))
            for key in offspring:
                if key in next_pop:
                    next_pop[key] += offspring[key]
                else:
                    next_pop[key] = offspring[key]
        current_pop = next_pop
        counter += 1
        print("generation: " + str(counter))
    return current_pop


print(generate_offspring('T t', 't t', 100))

print(garden_simulation({'T t': 1, 't t': 1}, n_crosses=10, n_generations=10, max_pop_size=1000))
