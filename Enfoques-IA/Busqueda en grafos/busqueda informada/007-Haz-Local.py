# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import random

def objective_function(x):
    """
    Función objetivo para maximizar.
    En este ejemplo, utilizaremos la función cuadrática f(x) = -x^2.
    """
    return -x**2

def hill_climbing_search():
    # Parámetros de la búsqueda de Haz Local
    num_neighbors = 10   # Número de vecinos generados en cada iteración
    
    # Generación del estado inicial
    current_state = random.uniform(-10, 10)
    current_cost = objective_function(current_state)
    
    while True:
        # Generación de vecinos
        neighbors = []
        for _ in range(num_neighbors):
            neighbor_state = current_state + random.uniform(-1, 1)
            neighbor_cost = objective_function(neighbor_state)
            neighbors.append((neighbor_state, neighbor_cost))
        
        # Selección del mejor vecino
        best_neighbor = max(neighbors, key=lambda x: x[1])
        
        # Comprobación de si se ha alcanzado el óptimo local
        if best_neighbor[1] <= current_cost:
            break
        
        # Actualización del estado actual
        current_state = best_neighbor[0]
        current_cost = best_neighbor[1]
    
    return current_state, current_cost

# Ejecución de la búsqueda de Haz Local
best_state, best_cost = hill_climbing_search()

print("Mejor estado:", best_state)
print("Mejor costo:", best_cost)
