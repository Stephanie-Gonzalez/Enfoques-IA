# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

class KohonenMap:
    def __init__(self, input_size, output_size, learning_rate=0.1, sigma=1.0):
        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate
        self.sigma = sigma
        self.weights = np.random.randn(output_size[0], output_size[1], input_size)
    
    def train(self, input_data, epochs):
        for _ in range(epochs):
            for x in input_data:
                best_match_idx = self.find_best_match(x)
                self.update_weights(x, best_match_idx)
    
    def find_best_match(self, x):
        distances = np.sum((self.weights - x) ** 2, axis=2)
        best_match_idx = np.unravel_index(np.argmin(distances), distances.shape)
        return best_match_idx
    
    def update_weights(self, x, best_match_idx):
        for i in range(self.output_size[0]):
            for j in range(self.output_size[1]):
                weight = self.weights[i, j]
                distance = np.sqrt((i - best_match_idx[0]) ** 2 + (j - best_match_idx[1]) ** 2)
                influence = np.exp(-distance / (2 * self.sigma ** 2))
                weight += self.learning_rate * influence * (x - weight)
                self.weights[i, j] = weight

# Ejemplo de uso
input_data = np.array([[0.2, 0.8], [0.6, 0.4], [0.5, 0.7], [0.3, 0.2]])

map_size = (5, 5)
input_size = input_data.shape[1]

kohonen_map = KohonenMap(input_size, map_size)
kohonen_map.train(input_data, epochs=1000)

# Evaluación
for x in input_data:
    best_match_idx = kohonen_map.find_best_match(x)
    print(f"Entrada: {x}, Mejor coincidencia: {best_match_idx}")
