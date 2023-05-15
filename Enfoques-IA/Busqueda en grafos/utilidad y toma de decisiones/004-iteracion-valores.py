# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Definir la matriz de recompensas
rewards = np.array([[-1, -1, -1, 0],
                    [-1, -1, -1, -1],
                    [-1, -1, -1, -1],
                    [10, -1, -1, -1]])

# Definir el factor de descuento
discount_factor = 0.9

# Inicializar los valores de utilidad
values = np.zeros(rewards.shape)

# Realizar la iteración de valores
while True:
    prev_values = np.copy(values)
    for i in range(rewards.shape[0]):
        for j in range(rewards.shape[1]):
            if i == rewards.shape[0] - 1 and j == rewards.shape[1] - 1:
                values[i, j] = rewards[i, j]
            else:
                values[i, j] = rewards[i, j] + discount_factor * max(values[i+1, j], values[i, j+1])
    if np.max(np.abs(values - prev_values)) < 1e-6:
        break

# Imprimir los valores de utilidad resultantes
print("Valores de Utilidad:")
print(values)
