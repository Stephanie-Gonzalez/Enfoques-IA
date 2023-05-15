# -*- coding: utf-8 -*-
"""

@author: sttep
"""

from skimage import io, filters

# Cargar la imagen
image = io.imread('imagen.jpg', as_gray=True)

# Aplicar el filtro de desenfoque
blurred_image = filters.gaussian(image, sigma=1)

# Mostrar la imagen original y la imagen desenfocada
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Imagen Original')
axes[0].axis('off')
axes[1].imshow(blurred_image, cmap='gray')
axes[1].set_title('Imagen Desenfocada')
axes[1].axis('off')

# Mostrar el resultado
plt.show()
