# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

class Adaline:
    def __init__(self, tasa_aprendizaje=0.01, epocas=50):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = None
        self.sesgo = None

    def ajustar(self, X, y):
        # Inicializar los pesos y el sesgo con valores aleatorios pequeños
        self.pesos = np.random.randn(X.shape[1])
        self.sesgo = np.random.randn()

        for _ in range(self.epocas):
            # Calcular la salida del modelo
            y_pred = self.predecir(X)

            # Actualizar los pesos y el sesgo mediante el descenso del gradiente
            self.pesos += self.tasa_aprendizaje * np.dot(X.T, (y - y_pred))
            self.sesgo += self.tasa_aprendizaje * np.sum(y - y_pred)

    def predecir(self, X):
        # Calcular la salida del modelo
        z = np.dot(X, self.pesos) + self.sesgo
        y_pred = np.where(z >= 0, 1, -1)
        return y_pred
    
    
###########################################################
import numpy as np

class Madaline:
    def __init__(self, tasa_aprendizaje=0.01, epocas=50):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = None
        self.sesgo = None

    def ajustar(self, X, y):
        # Inicializar los pesos y el sesgo con valores aleatorios pequeños
        self.pesos = np.random.randn(X.shape[1])
        self.sesgo = np.random.randn()

        for _ in range(self.epocas):
            # Calcular la salida del modelo
            y_pred = self.predecir(X)

            # Actualizar los pesos y el sesgo mediante el descenso del gradiente
            self.pesos += self.tasa_aprendizaje * np.dot(X.T, (y - y_pred))
            self.sesgo += self.tasa_aprendizaje * np.sum(y - y_pred)

    def predecir(self, X):
        # Calcular la salida del modelo
        z = np.dot(X, self.pesos) + self.sesgo
        y_pred = np.where(z >= 0, 1, 0)
        return y_pred
