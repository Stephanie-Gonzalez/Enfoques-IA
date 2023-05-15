# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Definición del entorno del juego
num_estados = 6
num_acciones = 4

# Definición de las recompensas y transiciones del entorno
recompensas = np.array([[-1, -1, -1, -1],
                        [-1, -1, -1, -1],
                        [-1, -1, -1, -1],
                        [-1, -1, -1, 100],
                        [-1, -1, -1, -1],
                        [-1, -1, -1, -1]])

transiciones = np.array([[0, 1, 1, 0],
                         [1, 0, 0, 1],
                         [1, 0, 0, 1],
                         [0, 1, 1, 0],
                         [1, 0, 0, 1],
                         [1, 0, 0, 1]])

# Definición de los parámetros de aprendizaje
num_episodios = 1000
factor_aprendizaje = 0.8
factor_descuento = 0.95

# Inicialización de la matriz Q
Q = np.zeros((num_estados, num_acciones))

# Función para seleccionar una acción basada en la matriz Q y la política ε-greedy
def seleccionar_accion(estado, epsilon):
    if np.random.uniform() < epsilon:
        return np.random.randint(num_acciones)
    else:
        return np.argmax(Q[estado])

# Aprendizaje por Q-Learning
for episodio in range(num_episodios):
    estado_actual = np.random.randint(0, num_estados)
    
    while estado_actual != 3:
        accion = seleccionar_accion(estado_actual, epsilon=0.2)
        nuevo_estado = np.random.choice(range(num_estados), p=transiciones[estado_actual][accion])
        
        # Actualización de la matriz Q
        Q[estado_actual][accion] = Q[estado_actual][accion] + factor_aprendizaje * (recompensas[estado_actual][accion] + factor_descuento * np.max(Q[nuevo_estado]) - Q[estado_actual][accion])
        
        estado_actual = nuevo_estado

# Impresión de la matriz Q aprendida
print("Matriz Q aprendida:")
print(Q)
