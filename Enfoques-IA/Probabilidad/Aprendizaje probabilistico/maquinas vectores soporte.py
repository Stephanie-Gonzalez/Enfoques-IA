# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Restablecer la configuración de errores de NumPy
np.seterr(all='warn')

# Cargar el conjunto de datos de dígitos escritos a mano (MNIST)
digits = load_digits()
X, y = digits.data, digits.target

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador SVM con núcleo
svm = SVC(kernel='rbf')

# Entrenar el clasificador SVM
svm.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = svm.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del SVM:", accuracy)
