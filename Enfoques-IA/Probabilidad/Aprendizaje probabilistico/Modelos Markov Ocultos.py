# -*- coding: utf-8 -*-
"""

@author: sttep
"""


from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos de ejemplo (iris)
iris = load_iris()
X, y = iris.data, iris.target

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador k-NN
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenar el clasificador k-NN
knn.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba con k-NN
y_pred_knn = knn.predict(X_test)

# Calcular la precisión del clasificador k-NN
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print("Precisión del k-NN:", accuracy_knn)

# Crear el modelo k-Means con k=3 (número de clusters)
kmeans = KMeans(n_clusters=3, random_state=42)

# Ajustar el modelo k-Means a los datos
kmeans.fit(X)

# Obtener las etiquetas de los clusters asignados a cada muestra con k-Means
labels_kmeans = kmeans.labels_
print("Etiquetas de los clusters (k-Means):", labels_kmeans)

# Crear el modelo de clustering jerárquico aglomerativo con 3 clusters
clustering = AgglomerativeClustering(n_clusters=3)

# Ajustar el modelo de clustering jerárquico a los datos
clustering.fit(X)

# Obtener las etiquetas de los clusters asignados a cada muestra con clustering jerárquico
labels_clustering = clustering.labels_
print("Etiquetas de los clusters (Clustering jerárquico):", labels_clustering)
