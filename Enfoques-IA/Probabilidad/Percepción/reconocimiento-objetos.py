# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

# Cargar el modelo preentrenado de MobileNetV2
model = MobileNetV2(weights='imagenet')

# Cargar la imagen de prueba
img_path = 'imagen.jpg'
img = image.load_img(img_path, target_size=(224, 224))

# Preprocesar la imagen para que coincida con el formato de entrada del modelo
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Realizar la predicción
preds = model.predict(x)

# Decodificar las predicciones
decoded_preds = decode_predictions(preds, top=3)[0]

# Mostrar las predicciones
for pred in decoded_preds:
    print(f"Objeto: {pred[1]}, Probabilidad: {pred[2]*100}%")
