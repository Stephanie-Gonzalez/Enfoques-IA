# -*- coding: utf-8 -*-
"""

@author: sttep
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Genera un conjunto de datos de ejemplo
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)

# Entrena un modelo de clasificación
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Realiza predicciones sobre los datos de entrenamiento
predictions = model.predict(X)

# Calcula la incertidumbre
uncertainty = 1.0 - model.predict_proba(X).max(axis=1)

# Imprime la incertidumbre para cada predicción
for i in range(len(uncertainty)):
    print(f"Incertidumbre para la predicción {i}: {uncertainty[i]}")

