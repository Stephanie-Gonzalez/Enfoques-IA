# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

# Función de activación Leaky ReLU
def leaky_relu(x, alpha=0.01):
    return np.where(x >= 0, x, alpha * x)

# Función de activación ELU (Exponential Linear Unit)
def elu(x, alpha=1.0):
    return np.where(x >= 0, x, alpha * (np.exp(x) - 1))

# Función de activación Softplus
def softplus(x):
    return np.log(1 + np.exp(x))

# Función de activación Swish
def swish(x):
    return x * sigmoid(x)

# Ejemplo de uso
x = np.array([-2, -1, 0, 1, 2])

print("Leaky ReLU:", leaky_relu(x))
print("ELU:", elu(x))
print("Softplus:", softplus(x))
print("Swish:", swish(x))
