# -*- coding: utf-8 -*-
"""

@author: sttep
"""


import random

# Definir el modelo bayesiano
def bayesian_model():
    # Definir las variables y sus distribuciones
    variable_A = random.choice([True, False])
    variable_B_given_A = {True: 0.7, False: 0.3}
    variable_C_given_A = {True: 0.9, False: 0.2}

    # Generar una muestra aleatoria según el modelo
    sample = {'A': variable_A,
              'B': random.choices([True, False], [variable_B_given_A[variable_A], 1 - variable_B_given_A[variable_A]])[0],
              'C': random.choices([True, False], [variable_C_given_A[variable_A], 1 - variable_C_given_A[variable_A]])[0]}

    return sample

# Realizar la ponderación de verosimilitud
def likelihood_weighting(num_samples):
    counts = {'A': 0, 'B': 0, 'C': 0}

    for _ in range(num_samples):
        sample = bayesian_model()
        variable_B_given_A = {True: 0.7, False: 0.3}  # Distribución condicional actualizada para cada muestra
        variable_C_given_A = {True: 0.9, False: 0.2}  # Distribución condicional actualizada para cada muestra
        weight = sample['A'] * variable_B_given_A[sample['A']] * variable_C_given_A[sample['A']]
        
        counts['A'] += sample['A'] * weight
        counts['B'] += sample['B'] * weight
        counts['C'] += sample['C'] * weight
    
    # Normalizar los resultados
    total_weight = sum(counts.values())
    for var in counts:
        counts[var] /= total_weight
    
    return counts

# Ejemplo de uso
num_samples = 1000
results = likelihood_weighting(num_samples)
print("Probabilidad de A:", results['A'])
print("Probabilidad de B:", results['B'])
print("Probabilidad de C:", results['C'])

