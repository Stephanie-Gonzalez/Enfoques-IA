# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Algoritmo Hacia Delante-Atrás
def forward_backward(observations, transition_matrix, emission_matrix, initial_distribution):
    num_states = len(initial_distribution)
    num_observations = len(observations)

    # Paso hacia delante (Forward)
    forward_probabilities = np.zeros((num_observations, num_states))
    forward_probabilities[0] = initial_distribution * emission_matrix[:, observations[0]]

    for t in range(1, num_observations):
        for j in range(num_states):
            forward_probabilities[t, j] = np.sum(forward_probabilities[t-1] * transition_matrix[:, j]) * emission_matrix[j, observations[t]]

    # Paso hacia atrás (Backward)
    backward_probabilities = np.zeros((num_observations, num_states))
    backward_probabilities[-1] = 1

    for t in range(num_observations - 2, -1, -1):
        for i in range(num_states):
            backward_probabilities[t, i] = np.sum(backward_probabilities[t+1] * transition_matrix[i, :] * emission_matrix[:, observations[t+1]])

    # Calcular las probabilidades a posteriori
    posterior_probabilities = forward_probabilities * backward_probabilities
    posterior_probabilities /= np.sum(posterior_probabilities, axis=1, keepdims=True)

    return posterior_probabilities

# Ejemplo de uso
observations = [0, 1, 0, 1, 0]  # Observaciones
transition_matrix = np.array([[0.7, 0.3], [0.2, 0.8]])  # Matriz de transición
emission_matrix = np.array([[0.9, 0.1], [0.4, 0.6]])  # Matriz de emisión
initial_distribution = np.array([0.6, 0.4])  # Distribución inicial de los estados

# Aplicar el algoritmo Hacia Delante-Atrás
posterior_probs = forward_backward(observations, transition_matrix, emission_matrix, initial_distribution)

# Resultados
print("Probabilidades a posteriori:")
for t in range(len(observations)):
    print("Tiempo", t+1, ":", posterior_probs[t])
