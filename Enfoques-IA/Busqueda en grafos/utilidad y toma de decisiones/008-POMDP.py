# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Definir los estados posibles
states = ['S1', 'S2', 'S3']

# Definir las acciones posibles
actions = ['A1', 'A2']

# Definir las observaciones posibles
observations = ['O1', 'O2']

# Definir la matriz de transiciones estado-acción-estado
transitions = {
    'S1': {'A1': {'S1': 0.7, 'S2': 0.3}, 'A2': {'S1': 0.4, 'S2': 0.6}},
    'S2': {'A1': {'S1': 0.1, 'S2': 0.9}, 'A2': {'S1': 0.8, 'S2': 0.2}},
    'S3': {'A1': {'S1': 1.0, 'S2': 0.0}, 'A2': {'S1': 0.0, 'S2': 1.0}}
}

# Definir la matriz de observaciones estado-acción-observación
observations_matrix = {
    'S1': {'A1': {'O1': 0.8, 'O2': 0.2}, 'A2': {'O1': 0.3, 'O2': 0.7}},
    'S2': {'A1': {'O1': 0.6, 'O2': 0.4}, 'A2': {'O1': 0.1, 'O2': 0.9}},
    'S3': {'A1': {'O1': 0.0, 'O2': 1.0}, 'A2': {'O1': 0.0, 'O2': 1.0}}
}

# Definir la creencia inicial
initial_belief = np.array([1/3, 1/3, 1/3])

# Definir la función de actualización de creencia basada en la observación
def update_belief(belief, action, observation):
    new_belief = np.zeros(len(belief))
    for i, state in enumerate(states):
        observation_prob = observations_matrix[state][action].get(observation, 0)
        for j, prev_state in enumerate(states):
            transition_prob = transitions[prev_state][action].get(state, 0)
            new_belief[i] += belief[j] * transition_prob * observation_prob
    new_belief /= np.sum(new_belief)
    return new_belief

# Realizar una secuencia de acciones y observaciones
actions_sequence = ['A1', 'A2']
observations_sequence = ['O1', 'O2']

belief = initial_belief
for action, observation in zip(actions_sequence, observations_sequence):
    belief = update_belief(belief, action, observation)
    print(f'Belief after action {action} and observation {observation}: {belief}')
