# -*- coding: utf-8 -*-
"""

@author: sttep
"""

# Probabilidad a priori
probabilidad_A = 0.3  # Probabilidad inicial de que ocurra el evento A
probabilidad_B = 0.2  # Probabilidad inicial de que ocurra el evento B

# Probabilidad condicional
probabilidad_B_dado_A = 0.6  # Probabilidad de que ocurra el evento B dado que ha ocurrido el evento A

# Evidencia
probabilidad_B_total = probabilidad_B_dado_A * probabilidad_A + probabilidad_B * (1 - probabilidad_A)

# Probabilidad a posteriori
probabilidad_A_dado_B = (probabilidad_B_dado_A * probabilidad_A) / probabilidad_B_total

# Imprime el resultado
print("La probabilidad de A dado B es:", probabilidad_A_dado_B)
