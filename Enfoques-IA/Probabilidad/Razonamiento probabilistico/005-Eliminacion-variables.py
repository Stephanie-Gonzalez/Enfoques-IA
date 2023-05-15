# -*- coding: utf-8 -*-
"""

@author: sttep
"""

from sklearn.feature_selection import VarianceThreshold

# Datos de entrenamiento
X_train = [[1, 2, 1], [2, 1, 0], [3, 1, 1], [4, 1, 0], [5, 2, 1]]
y_train = [0, 1, 1, 0, 1]

# Crear un objeto selector de características
selector = VarianceThreshold(threshold=0.2)

# Ajustar el selector a los datos de entrenamiento
X_train_selected = selector.fit_transform(X_train)

# Obtener las características seleccionadas
feature_indices = selector.get_support(indices=True)

# Imprimir las características seleccionadas
selected_features = [feature for feature in X_train[0] if feature_indices.__contains__(X_train[0].index(feature))]
print("Características seleccionadas:", selected_features)

