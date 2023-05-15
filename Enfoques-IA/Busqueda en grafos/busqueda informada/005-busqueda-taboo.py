# -*- coding: utf-8 -*-
"""

@author: sttep
"""
import random
import sys

class TabuSearch:
    def __init__(self, distance_matrix, num_iterations, tabu_size):
        self.distance_matrix = distance_matrix
        self.num_iterations = num_iterations
        self.tabu_size = tabu_size

    def search(self):
        num_cities = len(self.distance_matrix)
        current_solution = self.generate_initial_solution(num_cities)
        best_solution = current_solution.copy()
        tabu_list = []

        for _ in range(self.num_iterations):
            neighbors = self.generate_neighbors(current_solution)
            best_neighbor = self.select_best_neighbor(neighbors, tabu_list)
            current_solution = best_neighbor

            if self.calculate_distance(best_neighbor) < self.calculate_distance(best_solution):
                best_solution = best_neighbor

            tabu_list.append(best_neighbor)
            if len(tabu_list) > self.tabu_size:
                tabu_list.pop(0)

        return best_solution

    def generate_initial_solution(self, num_cities):
        cities = list(range(num_cities))
        random.shuffle(cities)
        return cities

    def generate_neighbors(self, solution):
        neighbors = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbor = solution.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

    def select_best_neighbor(self, neighbors, tabu_list):
        best_neighbor = None
        best_distance = sys.maxsize

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                distance = self.calculate_distance(neighbor)
                if distance < best_distance:
                    best_distance = distance
                    best_neighbor = neighbor

        return best_neighbor

    def calculate_distance(self, solution):
        distance = 0
        for i in range(len(solution)):
            current_city = solution[i]
            next_city = solution[(i + 1) % len(solution)]
            distance += self.distance_matrix[current_city][next_city]
        return distance

# Ejemplo de uso
distance_matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]
num_iterations = 100
tabu_size = 10

tabu_search = TabuSearch(distance_matrix, num_iterations, tabu_size)
best_solution = tabu_search.search()

print("Mejor solución encontrada:", best_solution)
print("Distancia de la mejor solución:", tabu_search.calculate_distance(best_solution))

