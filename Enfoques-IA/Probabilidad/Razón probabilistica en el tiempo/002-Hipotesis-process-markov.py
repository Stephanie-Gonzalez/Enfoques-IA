# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Definir la matriz de transición del proceso de Markov
trans_matrix = np.array([[0.7, 0.3], [0.2, 0.8]])  # Ejemplo de matriz de transición

# Definir el estado inicial
initial_state = 0  # Ejemplo de estado inicial

# Simulación del proceso de Markov
num_steps = 10  # Número de pasos de tiempo a simular
current_state = initial_state

# Realizar la simulación
print("Simulación del proceso de Markov:")
print("Estado inicial:", current_state)

for step in range(num_steps):
    # Generar el siguiente estado basado en la matriz de transición
    next_state = np.random.choice([0, 1], p=trans_matrix[current_state])
    
    # Actualizar el estado actual
    current_state = next_state
    
    # Imprimir el estado actual
    print("Paso", step+1, "- Estado:", current_state)
