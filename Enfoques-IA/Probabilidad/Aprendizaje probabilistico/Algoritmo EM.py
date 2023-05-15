# -*- coding: utf-8 -*-
"""

@author: sttep
"""
import numpy as np

# Generar datos de ejemplo
np.random.seed(0)
observations = np.concatenate((np.random.normal(0, 1, 1000), np.random.normal(5, 1, 1000)))

# Inicializar los parámetros
mean1 = np.random.randn()
mean2 = np.random.randn()
std1 = np.random.rand()
std2 = np.random.rand()
weights = np.random.rand()

# Iterar hasta convergencia
max_iterations = 100
tolerance = 1e-4
for i in range(max_iterations):
    # E-step: Calcular las responsabilidades
    responsibility1 = weights * np.exp(-0.5 * ((observations - mean1) / std1) ** 2)
    responsibility2 = (1 - weights) * np.exp(-0.5 * ((observations - mean2) / std2) ** 2)
    total_responsibility = responsibility1 + responsibility2
    responsibility1 /= total_responsibility
    responsibility2 /= total_responsibility

    # M-step: Actualizar los parámetros
    weights = np.mean(responsibility1)
    mean1 = np.sum(responsibility1 * observations) / np.sum(responsibility1)
    mean2 = np.sum(responsibility2 * observations) / np.sum(responsibility2)
    std1 = np.sqrt(np.sum(responsibility1 * (observations - mean1) ** 2) / np.sum(responsibility1))
    std2 = np.sqrt(np.sum(responsibility2 * (observations - mean2) ** 2) / np.sum(responsibility2))

    # Verificar convergencia
    if np.abs(weights - 0.5) < tolerance and np.abs(mean1 - 0) < tolerance and np.abs(mean2 - 5) < tolerance:
        break

# Imprimir los parámetros aprendidos
print("Mean 1:", mean1)
print("Mean 2:", mean2)
print("Standard Deviation 1:", std1)
print("Standard Deviation 2:", std2)
print("Weight 1:", weights)
print("Weight 2:", 1 - weights)
