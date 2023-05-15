# -*- coding: utf-8 -*-
"""

@author: sttep
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import sobel

# Generación de una textura procedural utilizando ruido Perlin
def generate_texture(width, height, scale=10):
    # Generar una malla de coordenadas
    x = np.linspace(0, width, num=width)
    y = np.linspace(0, height, num=height)
    x_mesh, y_mesh = np.meshgrid(x, y)
    
    # Escalar las coordenadas para obtener detalles de textura
    x_scaled = x_mesh / scale
    y_scaled = y_mesh / scale
    
    # Calcular el ruido Perlin
    noise = np.sin(x_scaled) + np.cos(y_scaled)
    
    # Normalizar el ruido entre 0 y 1
    normalized_noise = (noise - np.min(noise)) / (np.max(noise) - np.min(noise))
    
    return normalized_noise

# Generación de sombras utilizando iluminación simple
def generate_shadows(texture):
    # Calcular el gradiente utilizando el operador Sobel
    gradient_x = sobel(texture, axis=0)
    gradient_y = sobel(texture, axis=1)
    
    # Calcular la dirección de la luz como la inversa del gradiente
    light_directions = np.stack((-gradient_x, -gradient_y), axis=-1)
    
    # Normalizar el vector de dirección de la luz
    light_magnitudes = np.linalg.norm(light_directions, axis=-1)
    light_directions = light_directions / light_magnitudes[..., np.newaxis]
    
    return light_directions

# Tamaño de la textura
width = 256
height = 256

# Generar la textura procedural
texture = generate_texture(width, height)

# Generar sombras en la textura
shadows = generate_shadows(texture)

# Mostrar la textura y las sombras generadas
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(texture, cmap='gray')
axs[0].set_title('Textura')
axs[0].axis('off')
axs[1].imshow(shadows, cmap='gray')
axs[1].set_title('Sombras')
axs[1].axis('off')

plt.show()
