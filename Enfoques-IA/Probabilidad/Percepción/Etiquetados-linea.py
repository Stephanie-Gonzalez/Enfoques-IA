# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import nltk

# Texto de ejemplo
texto = "Este es un ejemplo de texto con varias líneas. Cada línea será etiquetada de forma individual."

# Tokenizar el texto en líneas
lineas = texto.split('\n')

# Etiquetar cada línea
for linea in lineas:
    palabras = nltk.word_tokenize(linea)  # Tokenizar la línea en palabras
    etiquetas = nltk.pos_tag(palabras)  # Etiquetar las palabras
    print(etiquetas)
