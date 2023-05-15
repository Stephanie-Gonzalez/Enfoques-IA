# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.weights = [np.random.randn(layers[i], layers[i+1]) for i in range(len(layers)-1)]
        self.biases = [np.zeros((1, layers[i+1])) for i in range(len(layers)-1)]
    
    def feedforward(self, x):
        a = x
        for w, b in zip(self.weights, self.biases):
            z = np.dot(a, w) + b
            a = sigmoid(z)
        return a
    
    def train(self, x, y, learning_rate, epochs):
        for epoch in range(epochs):
            a = x
            activations = [a]
            zs = []
            for w, b in zip(self.weights, self.biases):
                z = np.dot(a, w) + b
                zs.append(z)
                a = sigmoid(z)
                activations.append(a)
            
            delta = (activations[-1] - y) * sigmoid_derivative(zs[-1])
            nabla_w = [np.dot(activations[-2].T, delta)]
            nabla_b = [np.sum(delta, axis=0, keepdims=True)]
            
            for l in range(2, len(self.layers)):
                delta = np.dot(delta, self.weights[-l+1].T) * sigmoid_derivative(zs[-l])
                nabla_w.insert(0, np.dot(activations[-l-1].T, delta))
                nabla_b.insert(0, np.sum(delta, axis=0, keepdims=True))
            
            for l in range(len(self.layers)-1):
                self.weights[l] -= learning_rate * nabla_w[l]
                self.biases[l] -= learning_rate * nabla_b[l]

# Ejemplo de uso
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

network = NeuralNetwork([2, 2, 1])
network.train(x, y, learning_rate=0.1, epochs=10000)

# Evaluación
predictions = network.feedforward(x)
print("Predicciones:")
print(predictions)
