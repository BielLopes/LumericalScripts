from myPYGAD import pygad
import numpy as np

counter = 0
def calc_sol(solution):
	return solution[0] + solution[1] + solution[2] + solution[3] + solution[4] + solution[5]

def fitness_func(solution, solution_idx):
	global counter
	global sol_per_pop

	fitness = calc_sol(solution)


	counter = counter + 1

	return fitness

fitness_function = fitness_func

num_generations = 2
num_parents_mating = 2

sol_per_pop = 3
num_genes = 6

parent_selection_type = "rws"
keep_parents = 1

crossover_type = "arithmetic"

mutation_type = "random"
mutation_percent_genes = 25
gene_space = [{'low': 50, 'high': 280}, {'low': 50, 'high': 280}, {'low': 50, 'high': 280}, {'low': 50, 'high': 280}, {'low': 0.5, 'high': 2}, [0, 1, 2, 3, 4, 5, 6, 7]]

ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       gene_space=gene_space)

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))

print("Sum of the best solution : {solution}".format(solution=np.sum(solution)))

ga_instance.plot_result()