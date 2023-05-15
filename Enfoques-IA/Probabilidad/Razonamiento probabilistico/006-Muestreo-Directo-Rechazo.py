# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import random

# Muestreo directo
def direct_sampling(elements, num_samples):
    samples = random.sample(elements, num_samples)
    return samples

# Muestreo por rechazo
def rejection_sampling(distribution, num_samples):
    samples = []
    while len(samples) < num_samples:
        sample = random.choice(list(distribution.keys()))
        probability = distribution[sample]
        if random.random() < probability:
            samples.append(sample)
    return samples

# Ejemplo de uso del muestreo directo
elements = [1, 2, 3, 4, 5]
num_samples_direct = 3
samples_direct = direct_sampling(elements, num_samples_direct)
print("Muestra directa:", samples_direct)

# Ejemplo de uso del muestreo por rechazo
distribution = {1: 0.2, 2: 0.4, 3: 0.3, 4: 0.1}
num_samples_rejection = 5
samples_rejection = rejection_sampling(distribution, num_samples_rejection)
print("Muestra por rechazo:", samples_rejection)
