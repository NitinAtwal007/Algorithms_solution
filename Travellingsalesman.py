#TRAVELLING SALESMAN PROBLEM SOLUTION by NITIN ATWAL

import random

cities = {
    "A": (0, 0),
    "B": (1, 2),
    "C": (3, 1),
    "D": (2, 4),
    "E": (1, 3)
}

population_size = 200
mutation_rate = 0.04
num_generations = 100

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def initialize_population():
    population = []
    cities_list = list(cities.keys())
    for _ in range(population_size):
        random.shuffle(cities_list)
        population.append(cities_list[:])
    return population

def calculate_fitness(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += distance(solution[i], solution[i + 1])
    total_distance += distance(solution[-1], solution[0])
    return 1 / total_distance 

def select_parents(population, k=3):
    return max(random.sample(population, k), key=calculate_fitness)

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    return child1, child2

def mutate(solution):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(solution)), 2)
        solution[idx1], solution[idx2] = solution[idx2], solution[idx1]

def genetic_algorithm():
    population = initialize_population()
    for generation in range(num_generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1 = select_parents(population)
            parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    best_solution = max(population, key=calculate_fitness)
    best_fitness = calculate_fitness(best_solution)
    return best_solution, 1 / best_fitness

best_route, best_distance = genetic_algorithm()
print("Best Route:", best_route)
print("Best Distance:", best_distance)
