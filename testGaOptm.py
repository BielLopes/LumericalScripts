import pygad
import numpy as np

counter = 0
def calc_sol(solution):
	return solution[0] + solution[1] + solution[2] + solution[3] + solution[4] + solution[5]

def fitness_func(solution, solution_idx):
	global counter
	global sol_per_pop

	fitness = calc_sol(solution)

	f = open('.\\searched\\testFile_'+str(int(counter/sol_per_pop))+'_'+str(solution_idx)+'.txt', 'a')
	f.write('1 - {1} | 2 - {2} | 3 - {3} | 4 - {4} | 5 - {5} | 6 - {6} => {res}\n'.replace('{1}', str(solution[0])).replace('{2}', str(solution[1])).replace('{3}', str(solution[2])).replace('{4}', str(solution[3])).replace('{5}', str(solution[4])).replace('{6}', str(solution[5])).replace('{res}', str(fitness)))
	f.close()

	counter = counter + 1

	return fitness

fitness_function = fitness_func

num_generations = 50
num_parents_mating = 20

sol_per_pop = 20
num_genes = 6

parent_selection_type = "rws"
keep_parents = 3

crossover_type = "single_point"

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