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

# Inicializar una política aleatoria
policy = np.random.randint(0, 4, size=rewards.shape)

# Función para evaluar una política dada y obtener los valores de utilidad
def evaluate_policy(policy):
    values = np.zeros(rewards.shape)
    while True:
        prev_values = np.copy(values)
        for i in range(rewards.shape[0]):
            for j in range(rewards.shape[1]):
                if i == rewards.shape[0] - 1 and j == rewards.shape[1] - 1:
                    values[i, j] = rewards[i, j]
                else:
                    action = policy[i, j]
                    if action == 0:  # Arriba
                        next_state = max(i - 1, 0), j
                    elif action == 1:  # Abajo
                        next_state = min(i + 1, rewards.shape[0] - 1), j
                    elif action == 2:  # Izquierda
                        next_state = i, max(j - 1, 0)
                    else:  # Derecha
                        next_state = i, min(j + 1, rewards.shape[1] - 1)
                    values[i, j] = rewards[i, j] + discount_factor * values[next_state]
        if np.max(np.abs(values - prev_values)) < 1e-6:
            break
    return values

# Función para mejorar una política dada utilizando los valores de utilidad
def improve_policy(values):
    policy = np.zeros(rewards.shape, dtype=int)
    for i in range(rewards.shape[0]):
        for j in range(rewards.shape[1]):
            if i == rewards.shape[0] - 1 and j == rewards.shape[1] - 1:
                continue
            actions = []
            for action in range(4):
                if action == 0:  # Arriba
                    next_state = max(i - 1, 0), j
                elif action == 1:  # Abajo
                    next_state = min(i + 1, rewards.shape[0] - 1), j
                elif action == 2:  # Izquierda
                    next_state = i, max(j - 1, 0)
                else:  # Derecha
                    next_state = i, min(j + 1, rewards.shape[1] - 1)
                actions.append(rewards[i, j] + discount_factor * values[next_state])
            policy[i, j] = np.argmax(actions)
    return policy

# Realizar la iteración de políticas
while True:
    values = evaluate_policy(policy)
    new_policy = improve_policy(values)
    if np.array_equal(new_policy, policy):
        break
    policy = new_policy

# Imprimir la política resultante
print("Política Óptima:")
print(policy)
