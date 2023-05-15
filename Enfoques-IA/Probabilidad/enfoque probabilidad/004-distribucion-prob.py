# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np
from scipy.stats import norm

# Genera una distribución normal con media 0 y desviación estándar 1
distribucion = norm(loc=0, scale=1)

# Genera valores de la distribución
valores = np.linspace(-3, 3, num=100)  # Rango de valores

# Calcula las probabilidades para cada valor
probabilidades = distribucion.pdf(valores)

# Imprime los valores y sus probabilidades
for valor, probabilidad in zip(valores, probabilidades):
    print(f"Valor: {valor:.2f}, Probabilidad: {probabilidad:.4f}")
