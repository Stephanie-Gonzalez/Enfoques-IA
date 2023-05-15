# -*- coding: utf-8 -*-
"""

@author: sttep
"""
#entorno de juego simple donde el agente debe aprender a 
#navegar en un laberinto

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

# Aprendizaje por Refuerzo Activo utilizando Q-Learning
for episodio in range(num_episodios):
    estado_actual = np.random.randint(0, num_estados)
    
    while estado_actual != 3:
        accion = np.argmax(Q[estado_actual])
        nuevo_estado = np.random.choice(range(num_estados), p=transiciones[estado_actual][accion])
        
        # Actualización de la matriz Q
        Q[estado_actual][accion] = Q[estado_actual][accion] + factor_aprendizaje * (recompensas[estado_actual][accion] + factor_descuento * np.max(Q[nuevo_estado]) - Q[estado_actual][accion])
        
        estado_actual = nuevo_estado

# Impresión de la matriz Q aprendida
print("Matriz Q aprendida:")
print(Q)

#numero fijo de episodios de aprendizaje utilizando el 
#algoritmo de Q-Learning. La matriz Q se inicializa con 
#ceros y se actualiza en cada paso del episodio según la 
#ecuación de actualización de Q-Learning. La política 
#óptima se puede obtener seleccionando la acción con el 
#valor máximo en la matriz Q para cada estado.
