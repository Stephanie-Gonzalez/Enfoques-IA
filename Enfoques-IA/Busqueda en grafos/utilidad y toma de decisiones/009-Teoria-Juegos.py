# -*- coding: utf-8 -*-
"""
Created on Fri May 12 22:50:00 2023

@author: sttep
"""

import numpy as np
import nashpy as nash

# Definir la matriz de pagos del juego
payoff_matrix = np.array([[3, 0], [5, 1]])

# Crear el juego utilizando la matriz de pagos
game = nash.Game(payoff_matrix)

# Encontrar el equilibrio de Nash del juego
equilibria = game.support_enumeration()

# Imprimir los equilibrios encontrados
for eq in equilibria:
    print(f"Equilibrium: {eq}")
