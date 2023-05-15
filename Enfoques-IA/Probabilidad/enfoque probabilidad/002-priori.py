# -*- coding: utf-8 -*-
"""

@author: sttep
"""
import numpy as np

# Datos de ejemplo
etiquetas = ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B']

# Calcula la probabilidad a priori de cada clase
total_muestras = len(etiquetas)
clases, counts = np.unique(etiquetas, return_counts=True)
probabilidades_a_priori = counts / total_muestras

# Imprime la probabilidad a priori de cada clase
for i, clase in enumerate(clases):
    print(f"Probabilidad a priori de la clase {clase}: {probabilidades_a_priori[i]}")

