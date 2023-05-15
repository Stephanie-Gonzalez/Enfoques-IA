# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Datos de ejemplo
variable_A = np.array([1, 2, 3, 4, 5])
variable_B = np.array([2, 4, 6, 8, 10])
variable_C = np.array([3, 6, 9, 12, 15])

# Verifica la independencia condicional de A y B dado C
independencia_condicional = True

# Comprueba la independencia condicional para cada par de valores
for a, b, c in zip(variable_A, variable_B, variable_C):
    if a + b != c:
        independencia_condicional = False
        break

# Imprime el resultado de la independencia condicional
if independencia_condicional:
    print("La variable A es independiente de la variable B dado C")
else:
    print("La variable A no es independiente de la variable B dado C")
