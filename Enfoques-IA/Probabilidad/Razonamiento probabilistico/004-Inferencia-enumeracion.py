# -*- coding: utf-8 -*-
"""

@author: sttep
"""

def inferencia_por_enumeracion(red_bayesiana, evidencia):
    """
    Realiza la inferencia por enumeración en una red bayesiana dada una evidencia.
    """
    variables = list(red_bayesiana.keys())
    variables.sort()  # Ordenar variables en orden lexicográfico
    
    q = {}
    
    for variable in variables:
        q[variable] = 0.0
    
    for xi in [True, False]:
        extend_evidencia = evidencia.copy()
        extend_evidencia.update({variables[0]: xi})
        q[variables[0]] += enumeracion_all(red_bayesiana, variables[1:], extend_evidencia)
    
    return normalize(q)

def enumeracion_all(red_bayesiana, variables, evidencia):
    """
    Realiza la enumeración recursiva en todas las variables restantes.
    """
    if len(variables) == 0:
        return 1.0
    
    Y = variables[0]
    
    if Y in evidencia:
        return red_bayesiana[Y].probabilidad(evidencia[Y], evidencia) * enumeracion_all(red_bayesiana, variables[1:], evidencia)
    else:
        suma = 0.0
        
        for yi in [True, False]:
            extend_evidencia = evidencia.copy()
            extend_evidencia.update({Y: yi})
            suma += red_bayesiana[Y].probabilidad(yi, evidencia) * enumeracion_all(red_bayesiana, variables[1:], extend_evidencia)
        
        return suma

def normalize(distribucion):
    """
    Normaliza una distribución de probabilidad.
    """
    total = sum(distribucion.values())
    
    for key in distribucion:
        distribucion[key] /= total
    
    return distribucion

# Clase que representa una variable en la red bayesiana
class Variable:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tabla = {}
    
    def agregar_probabilidad(self, valor, evidencia, probabilidad):
        self.tabla[tuple(evidencia.items())] = probabilidad
    
    def probabilidad(self, valor, evidencia):
        return self.tabla[tuple(evidencia.items())]

# Ejemplo de uso
red_bayesiana = {
    'A': Variable('A'),
    'B': Variable('B'),
    'C': Variable('C')
}

# Agregar probabilidades a la variable 'A'
red_bayesiana['A'].agregar_probabilidad(True, {}, 0.3)
red_bayesiana['A'].agregar_probabilidad(False, {}, 0.7)

# Agregar probabilidades a la variable 'B'
red_bayesiana['B'].agregar_probabilidad(True, {'A': True}, 0.9)
red_bayesiana['B'].agregar_probabilidad(True, {'A': False}, 0.2)
red_bayesiana['B'].agregar_probabilidad(False, {'A': True}, 0.1)
red_bayesiana['B'].agregar_probabilidad(False, {'A': False}, 0.8)

# Agregar probabilidades a la variable 'C'
red_bayesiana['C'].agregar_probabilidad(True, {'A': True}, 0.4)
red_bayesiana['C'].agregar_probabilidad(True, {'A': False}, 0.5)
red_bayesiana['C'].
