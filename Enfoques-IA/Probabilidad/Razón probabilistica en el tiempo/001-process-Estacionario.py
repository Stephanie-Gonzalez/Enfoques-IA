# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np
import matplotlib.pyplot as plt

# Generar proceso ARMA
def generar_proceso_ARMA(phi, theta, num_muestras):
    # Inicializar el proceso con ceros
    proceso = np.zeros(num_muestras)

    # Generar muestras del proceso ARMA
    for t in range(len(proceso)):
        if t < max(len(phi), len(theta)):
            # Inicializar el proceso con ruido blanco gaussiano
            proceso[t] = np.random.normal(0, 1)
        else:
            # Calcular el valor del proceso ARMA en el tiempo t
            ar_component = np.sum([phi[i] * proceso[t-i-1] for i in range(len(phi))])
            ma_component = np.sum([theta[i] * np.random.normal(0, 1) for i in range(len(theta))])
            proceso[t] = ar_component + ma_component

    return proceso

# Visualizar proceso ARMA
def visualizar_proceso_ARMA(proceso):
    plt.plot(proceso)
    plt.xlabel('Tiempo')
    plt.ylabel('Valor')
    plt.title('Proceso ARMA')
    plt.show()

# Parámetros del proceso ARMA
phi = [0.5, -0.2]  # Coeficientes del componente autoregresivo
theta = [0.8, -0.3]  # Coeficientes del componente de media móvil
num_muestras = 1000  # Número de muestras a generar

# Generar proceso ARMA
proceso = generar_proceso_ARMA(phi, theta, num_muestras)

# Visualizar proceso ARMA
visualizar_proceso_ARMA(proceso)

