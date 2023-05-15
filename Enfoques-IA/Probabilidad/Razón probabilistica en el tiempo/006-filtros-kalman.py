# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

def kalman_filter(observed_data, initial_state, initial_covariance, transition_matrix, transition_covariance, observation_matrix, observation_covariance):
    # Inicialización
    state = initial_state
    covariance = initial_covariance

    filtered_states = []
    filtered_covariances = []

    # Filtro de Kalman
    for observation in observed_data:
        # Predicción
        predicted_state = np.dot(transition_matrix, state)
        predicted_covariance = np.dot(np.dot(transition_matrix, covariance), transition_matrix.T) + transition_covariance

        # Actualización
        innovation = observation - np.dot(observation_matrix, predicted_state)
        innovation_covariance = np.dot(np.dot(observation_matrix, predicted_covariance), observation_matrix.T) + observation_covariance

        kalman_gain = np.dot(np.dot(predicted_covariance, observation_matrix.T), np.linalg.inv(innovation_covariance))
        state = predicted_state + np.dot(kalman_gain, innovation)
        covariance = np.dot(np.eye(len(state)) - np.dot(kalman_gain, observation_matrix), predicted_covariance)

        # Guardar los resultados filtrados
        filtered_states.append(state)
        filtered_covariances.append(covariance)

    return filtered_states, filtered_covariances

# Parámetros del filtro de Kalman
initial_state = np.array([0, 0])  # Estado inicial
initial_covariance = np.eye(2)   # Covarianza inicial
transition_matrix = np.array([[1, 1], [0, 1]])  # Matriz de transición
transition_covariance = np.eye(2)  # Covarianza de transición
observation_matrix = np.array([[1, 0]])  # Matriz de observación
observation_covariance = np.array([[1]])  # Covarianza de observación

# Datos observados
observed_data = np.array([1, 2, 3, 4, 5])

# Ejecutar el filtro de Kalman
filtered_states, filtered_covariances = kalman_filter(observed_data, initial_state, initial_covariance,
                                                      transition_matrix, transition_covariance,
                                                      observation_matrix, observation_covariance)

# Resultados
print("Estados filtrados:")
for state in filtered_states:
    print(state)

print("\nCovarianzas filtradas:")
for covariance in filtered_covariances:
    print(covariance)
