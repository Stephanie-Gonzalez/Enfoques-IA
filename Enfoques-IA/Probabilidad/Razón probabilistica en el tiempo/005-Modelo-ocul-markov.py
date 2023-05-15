# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Definir los estados ocultos
hidden_states = ['Soleado', 'Lluvioso']

# Definir los observables
observations = ['Caminar', 'Comprar', 'Lluvia', 'Descansar']

# Definir la matriz de transición
transition_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])

# Definir las probabilidades iniciales
initial_distribution = np.array([0.6, 0.4])

# Definir las probabilidades de emisión
emission_matrix = np.array([[0.1, 0.4, 0.2, 0.3], [0.6, 0.3, 0.1, 0.0]])

# Función para generar una secuencia de observaciones y estados ocultos
def generate_sequence(num_steps):
    states = []
    observations = []

    current_state = np.random.choice(len(hidden_states), p=initial_distribution)
    for _ in range(num_steps):
        states.append(current_state)
        
        # Asegurarse de que las probabilidades de emisión sean mayores que cero
        non_zero_emissions = np.where(emission_matrix[current_state] > 0)[0]
        observation = np.random.choice(non_zero_emissions)
        
        observations.append(observation)
        current_state = np.random.choice(len(hidden_states), p=transition_matrix[current_state])

    return states, observations

# Generar una secuencia de observaciones y estados ocultos
num_steps = 5
states, observations = generate_sequence(num_steps)

# Resultados
print("Secuencia de observaciones generada:", [observations[i] for i in range(num_steps)])
print("Secuencia de estados ocultos generada:", [hidden_states[states[i]] for i in range(num_steps)])
