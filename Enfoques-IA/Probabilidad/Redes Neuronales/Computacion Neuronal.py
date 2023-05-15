# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar los datos de entrenamiento y prueba
(datos_entrenamiento, etiquetas_entrenamiento), (datos_prueba, etiquetas_prueba) = mnist.load_data()

# Preprocesamiento de datos
datos_entrenamiento = datos_entrenamiento.reshape(60000, 784) / 255.0
datos_prueba = datos_prueba.reshape(10000, 784) / 255.0
etiquetas_entrenamiento = tf.keras.utils.to_categorical(etiquetas_entrenamiento, 10)
etiquetas_prueba = tf.keras.utils.to_categorical(etiquetas_prueba, 10)

# Crear el modelo de la red neuronal
modelo = Sequential()
modelo.add(Dense(128, activation='sigmoid', input_shape=(784,)))
modelo.add(Dense(10, activation='softmax'))

# Compilar el modelo
modelo.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(datos_entrenamiento, etiquetas_entrenamiento, batch_size=128, epochs=10, verbose=1)

# Evaluar el modelo
perdida, exactitud = modelo.evaluate(datos_prueba, etiquetas_prueba, verbose=1)
print(f"Perdida: {perdida}")
print(f"Exactitud: {exactitud}")
