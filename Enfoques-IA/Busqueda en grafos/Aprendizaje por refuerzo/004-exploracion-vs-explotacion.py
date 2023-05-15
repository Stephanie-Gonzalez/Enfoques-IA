# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Definición de los parámetros
num_acciones = 5
epsilon = 0.2

# Generación de valores aleatorios para las recompensas de cada acción
recompensas = np.random.randn(num_acciones)

# Función para seleccionar una acción basada en la estrategia de exploración vs. explotación
def seleccionar_accion():
    if np.random.uniform() < epsilon:
        return np.random.randint(num_acciones)
    else:
        return np.argmax(recompensas)

# Ejemplo de uso
num_intentos = 100

for intento in range(num_intentos):
    accion_seleccionada = seleccionar_accion()
    recompensa_obtenida = recompensas[accion_seleccionada]
    print("Intento:", intento, "Acción seleccionada:", accion_seleccionada, "Recompensa:", recompensa_obtenida)
