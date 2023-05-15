# -*- coding: utf-8 -*-
"""

@author: sttep
"""
import random
import math

def objective_function(x):
    """
    Función objetivo para minimizar.
    En este ejemplo, utilizaremos la función cuadrática f(x) = x^2.
    """
    return x**2

def simulated_annealing_search():
    # Parámetros del Temple Simulado
    initial_temperature = 100  # Temperatura inicial
    final_temperature = 0.1   # Temperatura final
    cooling_factor = 0.95     # Factor de enfriamiento
    num_iterations = 1000     # Número de iteraciones
    
    # Generación del estado inicial
    current_state = random.uniform(-10, 10)
    current_cost = objective_function(current_state)
    
    # Mejor solución encontrada
    best_state = current_state
    best_cost = current_cost
    
    # Bucle de Temple Simulado
    temperature = initial_temperature
    for _ in range(num_iterations):
        # Generación de un vecino aleatorio
        neighbor_state = current_state + random.uniform(-1, 1)
        neighbor_cost = objective_function(neighbor_state)
        
        # Cálculo de la diferencia de costos entre el vecino y el estado actual
        delta_cost = neighbor_cost - current_cost
        
        # Verificación de si se acepta el vecino como el nuevo estado actual
        if delta_cost < 0 or math.exp(-delta_cost / temperature) > random.uniform(0, 1):
            current_state = neighbor_state
            current_cost = neighbor_cost
        
        # Actualización de la mejor solución encontrada
        if current_cost < best_cost:
            best_state = current_state
            best_cost = current_cost
        
        # Enfriamiento de la temperatura
        temperature *= cooling_factor
    
    return best_state, best_cost

# Ejecución del algoritmo de Temple Simulado
best_state, best_cost = simulated_annealing_search()

print("Mejor estado:", best_state)
print("Mejor costo:", best_cost)
