# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import gym
import numpy as np

# Crear el entorno MDP
env = gym.make('FrozenLake-v0')

# Obtener el número de estados y acciones
num_states = env.observation_space.n
num_actions = env.action_space.n

# Inicializar la matriz de recompensas y transiciones
rewards = np.zeros((num_states, num_actions, num_states))
transitions = np.zeros((num_states, num_actions, num_states))

# Obtener las recompensas y transiciones del entorno
for state in range(num_states):
    for action in range(num_actions):
        for transition in env.P[state][action]:
            prob, next_state, reward, _ = transition
            rewards[state, action, next_state] = reward
            transitions[state, action, next_state] = prob

# Definir la función de valor para los estados
values = np.zeros(num_states)

# Definir el factor de descuento para el proceso de decisión de Markov
discount_factor = 0.9

# Realizar iteraciones para actualizar los valores de los estados
for _ in range(100):
    new_values = np.zeros(num_states)
    for state in range(num_states):
        q_values = []
        for action in range(num_actions):
            q_value = np.sum(transitions[state, action] * (rewards[state, action] + discount_factor * values))
            q_values.append(q_value)
        new_values[state] = np.max(q_values)
    values = new_values

# Imprimir los valores finales de los estados
for state in range(num_states):
    print(f'Value of state {state}: {values[state]}')
