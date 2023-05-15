# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico de dispersión
plt.scatter(x, y)

# Configurar etiquetas y título del gráfico
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Dispersión')

# Mostrar el gráfico
plt.show()
