# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import random

def hill_climbing(problem):
    current_state = problem.initialize()  # Estado inicial
    while True:
        neighbors = problem.generate_neighbors(current_state)  # Genera estados vecinos
        best_neighbor = max(neighbors, key=lambda state: problem.evaluate(state))  # Selecciona el mejor vecino
        if problem.evaluate(best_neighbor) <= problem.evaluate(current_state):
            # Si el mejor vecino no mejora la solución actual, termina y devuelve la solución actual
            return current_state
        current_state = best_neighbor  # Actualiza el estado actual con el mejor vecino

# Ejemplo de problema de optimización
class OptimizationProblem:
    def initialize(self):
        # Aquí se debe implementar la generación del estado inicial
        pass

    def generate_neighbors(self, state):
        # Aquí se debe implementar la generación de los estados vecinos dado un estado
        pass

    def evaluate(self, state):
        # Aquí se debe implementar la función de evaluación del estado
        pass

# Ejemplo de problema específico que hereda de OptimizationProblem
class ExampleProblem(OptimizationProblem):
    def initialize(self):
        return random.randint(1, 100)  # Estado inicial aleatorio entre 1 y 100

    def generate_neighbors(self, state):
        neighbors = []
        for _ in range(5):  # Genera 5 estados vecinos
            neighbor = random.randint(state - 10, state + 10)  # Realiza una pequeña modificación
            neighbors.append(neighbor)
        return neighbors

    def evaluate(self, state):
        # La función de evaluación puede ser cualquier métrica que se desee optimizar
        return -abs(state - 50)  # Objetivo: minimizar la distancia al valor 50

# Ejemplo de uso
problem = ExampleProblem()
solution = hill_climbing(problem)
print("Solución encontrada:", solution)
