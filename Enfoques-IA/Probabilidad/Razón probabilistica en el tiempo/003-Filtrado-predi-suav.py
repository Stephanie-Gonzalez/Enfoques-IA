# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Filtro de Kalman
def kalman_filter(measurements):
    # Inicialización de variables
    initial_state = measurements[0]
    initial_covariance = 1.0
    state = initial_state
    covariance = initial_covariance
    filtered_states = []
    
    # Actualización y predicción
    for measurement in measurements:
        # Actualización del estado
        kalman_gain = covariance / (covariance + 1.0)
        state = state + kalman_gain * (measurement - state)
        
        # Actualización de la covarianza
        covariance = (1 - kalman_gain) * covariance
        
        # Guardar el estado filtrado
        filtered_states.append(state)
        
        # Predicción del siguiente estado
        state = state
        covariance = covariance + 1.0
        
    return filtered_states

# Predicción
def predict_next_state(filtered_states):
    return filtered_states[-1]

# Suavizado
def smooth_states(filtered_states):
    smoothed_states = []
    num_states = len(filtered_states)
    
    for i in range(num_states-1, -1, -1):
        if i == num_states-1:
            smoothed_states.insert(0, filtered_states[i])
        else:
            smoothed_state = filtered_states[i] + (smoothed_states[0] - filtered_states[i]) * (1.0 / (1.0 + 1.0))
            smoothed_states.insert(0, smoothed_state)
    
    return smoothed_states

# Explicación
def explain_states(filtered_states, smoothed_states):
    explained_states = []
    num_states = len(filtered_states)
    
    for i in range(num_states):
        explained_state = filtered_states[i] + (smoothed_states[i] - filtered_states[i]) * (1.0 / (1.0 + 1.0))
        explained_states.append(explained_state)
    
    return explained_states

#
