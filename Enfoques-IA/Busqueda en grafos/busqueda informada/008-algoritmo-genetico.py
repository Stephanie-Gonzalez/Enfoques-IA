# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import random

# Parámetros del algoritmo genético
population_size = 100     # Tamaño de la población
chromosome_length = 10    # Longitud de los cromosomas
mutation_rate = 0.01      # Tasa de mutación

# Función objetivo
def fitness_function(chromosome):
    """
    Función objetivo para maximizar.
    En este ejemplo, utilizaremos la función cuadrática f(x) = -x^2.
    """
    x = int(''.join(map(str, chromosome)), 2)  # Convertir el cromosoma binario a un número entero
    return -x**2

# Función de selección por torneo
def selection(population):
    tournament_size = 5  # Tamaño del torneo
    tournament = random.sample(population, tournament_size)
    winner = max(tournament, key=lambda x: fitness_function(x))
    return winner

# Función de cruce (crossover)
def crossover(parent1, parent2):
    point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Función de mutación
def mutation(chromosome):
    for i in range(chromosome_length):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # Mutación de un bit (cambio de 0 a 1 o viceversa)
    return chromosome

# Creación de la población inicial
population = []
for _ in range(population_size):
    chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
    population.append(chromosome)

# Evolución de la población
num_generations = 100
for generation in range(num_generations):
    # Evaluación de la aptitud de la población actual
    fitness_scores = [fitness_function(chromosome) for chromosome in population]
    
    # Selección de padres
    parents = [selection(population) for _ in range(population_size)]
    
    # Operadores de cruce y mutación
    offspring = []
    for i in range(0, population_size, 2):
        parent1 = parents[i]
        parent2 = parents[i+1]
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        offspring.extend([child1, child2])
    
    # Reemplazo de la población anterior con la descendencia generada
    population = offspring

# Obtención del mejor individuo
best_individual = max(population, key=lambda x: fitness_function(x))
best_fitness = fitness_function(best_individual)

print("Mejor individuo:", best_individual)
print("Mejor fitness:", best_fitness)
