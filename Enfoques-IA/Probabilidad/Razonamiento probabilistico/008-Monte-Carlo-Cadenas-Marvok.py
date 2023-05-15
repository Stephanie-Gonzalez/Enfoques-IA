# -*- coding: utf-8 -*-
"""
   
@author: sttep
"""

import random

# Definir el modelo de cadena de Markov
def markov_chain_model():
    # Definir las variables y sus distribuciones condicionales
    variable_A = random.choice([True, False])
    variable_B_given_A = {True: 0.7, False: 0.3}
    variable_C_given_A = {True: 0.9, False: 0.2}

    return variable_A, variable_B_given_A, variable_C_given_A

# Realizar el muestreo de Gibbs para el algoritmo MCMC
def gibbs_sampling(num_samples):
    counts = {'A': 0, 'B': 0, 'C': 0}
    variable_A, variable_B_given_A, variable_C_given_A = markov_chain_model()

    for _ in range(num_samples):
        # Actualizar la variable A
        variable_A = random.choices([True, False], [variable_B_given_A[True], variable_B_given_A[False]])[0]
        
        # Actualizar la variable B
        variable_B = random.choices([True, False], [variable_B_given_A[variable_A], 1 - variable_B_given_A[variable_A]])[0]
        
        # Actualizar la variable C
        variable_C = random.choices([True, False], [variable_C_given_A[variable_A], 1 - variable_C_given_A[variable_A]])[0]
        
        # Contar las ocurrencias
        counts['A'] += variable_A
        counts['B'] += variable_B
        counts['C'] += variable_C
    
    # Calcular las probabilidades
    total_samples = float(num_samples)
    counts['A'] /= total_samples
    counts['B'] /= total_samples
    counts['C'] /= total_samples
    
    return counts

# Ejemplo de uso
num_samples = 1000
results = gibbs_sampling(num_samples)
print("Probabilidad de A:", results['A'])
print("Probabilidad de B:", results['B'])
print("Probabilidad de C:", results['C'])
