# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Datos de ejemplo
etiquetas = ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B']
eventos_condicionantes = ['A', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A']
clase_objetivo = 'A'

# Calcula la probabilidad condicionada de la clase objetivo dado el evento condicionante
etiquetas = np.array(etiquetas)
eventos_condicionantes = np.array(eventos_condicionantes)
clase_objetivo = np.array(clase_objetivo)

# Filtra las etiquetas que coinciden con el evento condicionante
etiquetas_filtradas = etiquetas[eventos_condicionantes == clase_objetivo]

# Calcula la probabilidad condicionada
prob_condicionada = len(etiquetas_filtradas) / len(etiquetas)

# Normaliza la probabilidad condicionada
prob_condicionada_normalizada = prob_condicionada / np.sum(prob_condicionada)

# Imprime la probabilidad condicionada y normalizada
print(f"Probabilidad condicionada: {prob_condicionada}")
print(f"Probabilidad condicionada normalizada: {prob_condicionada_normalizada}")
