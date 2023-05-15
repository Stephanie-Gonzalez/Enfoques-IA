# -*- coding: utf-8 -*-
"""

@author: sttep
"""

#metodo Monte Carlo entorno de juego simple 
#donde el agente debe aprender a elegir 
#entre dos acciones: "izquierda" y "derecha"


import numpy as np

# Definición del entorno del juego
num_estados = 5
num_acciones = 2

# Inicialización de la matriz de recompensas
recompensas = np.array([[0, 0],
                       [0, 0],
                       [0, 0],
                       [0, 0],
                       [1, 0]])

# Definición de la política inicial
politica = np.array([[0.5, 0.5],
                     [0.5, 0.5],
                     [0.5, 0.5],
                     [0.5, 0.5],
                     [0.5, 0.5]])

# Definición de los parámetros de aprendizaje
num_episodios = 1000
factor_descuento = 0.9

# Aprendizaje por Refuerzo Pasivo utilizando el método de Monte Carlo
for episodio in range(num_episodios):
    estados_visitados = []
    recompensas_episodio = []
    
    estado_actual = np.random.randint(0, num_estados)
    while True:
        accion = np.random.choice(range(num_acciones), p=politica[estado_actual])
        nuevo_estado = accion
        
        estados_visitados.append(estado_actual)
        recompensas_episodio.append(recompensas[estado_actual][accion])
        
        if nuevo_estado == num_estados - 1:
            break
        
        estado_actual = nuevo_estado
    
    # Actualización de la política
    for t in range(len(estados_visitados)):
        estado = estados_visitados[t]
        accion = politica[estado].argmax()
        
        politica[estado] = 0
        politica[estado][accion] = 1
    
    # Actualización de las recompensas esperadas
    for t in range(len(estados_visitados)):
        estado = estados_visitados[t]
        accion = politica[estado].argmax()
        
        recompensas[estado][accion] += factor_descuento ** t * sum(recompensas_episodio[t:])


#el algoritmo realiza un número fijo de episodios de aprendizaje 
#aprendizaje y utiliza la política inicial para seleccionar
#acciones en cada paso. Después de cada episodio se 
#actualiza la política y las recompensas esperadas 
#utilizando el método de Monte Carlo.
#
