import numpy as np
import random
import math
import json

POPULATION_SIZE = 50
MUTATION_RATE = 0.01
NUM_GENERATIONS = 1000
GRID_SIZE = (100, 100)

start = (0, 0)
end = (51, 51)

def load_obstacles(filename='./data/sample_data.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    weather_conditions = data['weather'][0]['main']
    obstacles = []
    if weather_conditions in ['Rain', 'Snow', 'Fog', 'Clouds']:
        # print (weather_conditions)
        obstacles = [(i, i) for i in range(10, 20)]
    # print(data['weather'][0]['main'])
    # print(obstacles)
    return obstacles

obstacles = load_obstacles()

def create_chromosome():
    path = [start]
    for _ in range(1, GRID_SIZE[0]):
        next_step = (path[-1][0] + random.choice([0, 1]), path[-1][1] + random.choice([0, 1]))
        path.append(next_step)
    return path

def initialize_population():
    return [create_chromosome() for _ in range(POPULATION_SIZE)]

def fitness(chromosome):
    if chromosome[-1] != end:
        return float('inf')
    total_distance = sum(math.dist(chromosome[i], chromosome[i+1]) for i in range(len(chromosome)-1))
    obstacle_penalty = sum(1 for point in chromosome if point in obstacles)
    return total_distance + (obstacle_penalty * 1000)

def selection(population):
    population = sorted(population, key=lambda x: fitness(x))
    return population[:POPULATION_SIZE//2]

def crossover(parent1, parent2):
    cut = random.randint(1, len(parent1)-1)
    child = parent1[:cut] + parent2[cut:]
    return child

def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        index = random.randint(1, len(chromosome)-2)
        chromosome[index] = (chromosome[index][0] + random.choice([0, 1]), chromosome[index][1] + random.choice([0, 1]))
    return chromosome

def genetic_algorithm():
    population = initialize_population()
    for generation in range(NUM_GENERATIONS):
        selected_population = selection(population)
        next_population = selected_population[:]
        while len(next_population) < POPULATION_SIZE:
            parent1, parent2 = random.sample(selected_population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_population.append(child)
        population = next_population
    best_path = min(population, key=lambda x: fitness(x))
    return best_path
