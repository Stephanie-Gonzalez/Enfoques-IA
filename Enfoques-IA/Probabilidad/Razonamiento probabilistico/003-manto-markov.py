# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import random

class MarkovChain:
    def __init__(self):
        self.transitions = {}
        
    def agregar_transicion(self, estado_actual, estado_siguiente, probabilidad):
        if estado_actual not in self.transitions:
            self.transitions[estado_actual] = {}
        
        self.transitions[estado_actual][estado_siguiente] = probabilidad
    
    def generar_estado_siguiente(self, estado_actual):
        if estado_actual not in self.transitions:
            return None
        
        opciones = list(self.transitions[estado_actual].keys())
        probabilidades = list(self.transitions[estado_actual].values())
        estado_siguiente = random.choices(opciones, weights=probabilidades)[0]
        return estado_siguiente
    
    def generar_secuencia(self, estado_inicial, longitud):
        secuencia = [estado_inicial]
        estado_actual = estado_inicial
        
        for _ in range(longitud - 1):
            estado_siguiente = self.generar_estado_siguiente(estado_actual)
            
            if estado_siguiente is None:
                break
            
            secuencia.append(estado_siguiente)
            estado_actual = estado_siguiente
        
        return secuencia

# Ejemplo de uso
cadena_markov = MarkovChain()

cadena_markov.agregar_transicion('A', 'B', 0.6)
cadena_markov.agregar_transicion('A', 'C', 0.4)
cadena_markov.agregar_transicion('B', 'C', 0.8)
cadena_markov.agregar_transicion('B', 'D', 0.2)
cadena_markov.agregar_transicion('C', 'A', 0.3)
cadena_markov.agregar_transicion('C', 'B', 0.7)
cadena_markov.agregar_transicion('D', 'D', 1.0)

secuencia_generada = cadena_markov.generar_secuencia('A', 10)
print("Secuencia generada:", secuencia_generada)
