# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.priors = np.zeros(len(self.classes))
        self.likelihoods = []

        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            self.priors[i] = X_c.shape[0] / X.shape[0]
            likelihood = np.mean(X_c, axis=0)
            self.likelihoods.append(likelihood)

    def predict(self, X):
        y_pred = []

        for x in X:
            posteriors = []

            for i, c in enumerate(self.classes):
                prior = np.log(self.priors[i])
                likelihood = np.sum(np.log(self.calculate_likelihood(x, self.likelihoods[i])))
                posterior = prior + likelihood
                posteriors.append(posterior)

            y_pred.append(self.classes[np.argmax(posteriors)])

        return y_pred

    def calculate_likelihood(self, x, likelihood):
        return np.exp(-((x - likelihood) ** 2) / (2 * (np.var(likelihood) + 1e-6)))

# Datos de ejemplo
X = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1]
])
y = np.array([1, 1, 0, 0])

# Instanciar y entrenar el clasificador Naïve Bayes
classifier = NaiveBayes()
classifier.fit(X, y)

# Datos de prueba
X_test = np.array([[1, 0, 1], [0, 1, 1]])

# Realizar predicciones
y_pred = classifier.predict(X_test)

# Imprimir predicciones
for i in range(len(y_pred)):
    print(f"Predicción para el ejemplo {i + 1}: {y_pred[i]}")
