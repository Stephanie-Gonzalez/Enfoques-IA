# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import cv2
import numpy as np

# Cargar la imagen en escala de grises
image = cv2.imread('imagen.jpg', 0)

# Aplicar el detector de bordes Canny
edges = cv2.Canny(image, 100, 200)

# Aplicar la segmentación mediante umbralización
_, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Mostrar la imagen original, los bordes detectados y la imagen segmentada
cv2.imshow("Imagen Original", image)
cv2.imshow("Bordes Detectados", edges)
cv2.imshow("Imagen Segmentada", thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()
