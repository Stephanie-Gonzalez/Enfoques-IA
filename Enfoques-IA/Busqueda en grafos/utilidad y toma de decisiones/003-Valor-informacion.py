# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import math

def value_of_information(probabilities, utilities):
    voi = 0.0
    for outcome, probability in probabilities.items():
        expected_utility = 0.0
        for utility in utilities[outcome]:
            expected_utility += utility * probabilities[outcome]
        voi += probability * math.log(expected_utility, 2)
    return voi

# Ejemplo de probabilidades y utilidades
probabilities = {'Outcome1': 0.2, 'Outcome2': 0.3, 'Outcome3': 0.5}
utilities = {'Outcome1': [10, 20, 30], 'Outcome2': [15, 25, 35], 'Outcome3': [5, 10, 15]}

# Calcular el Valor de la Información
voi = value_of_information(probabilities, utilities)
print("Valor de la Información:", voi)
