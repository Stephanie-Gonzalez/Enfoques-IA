# -*- coding: utf-8 -*-
"""

@author: sttep
"""

# Datos de ejemplo
p_A = 0.6  # Probabilidad de A
p_B_given_A = 0.3  # Probabilidad de B dado A
p_C_given_A_B = 0.8  # Probabilidad de C dado A y B

# Calcular la probabilidad conjunta utilizando la regla de la cadena
p_joint = p_A * p_B_given_A * p_C_given_A_B

# Imprimir el resultado
print("La probabilidad conjunta P(A, B, C) es:", p_joint)
