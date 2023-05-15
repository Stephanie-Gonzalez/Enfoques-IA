# -*- coding: utf-8 -*-
"""

@author: sttep
"""

import speech_recognition as sr

# Crear un reconocedor de voz
r = sr.Recognizer()

# Abrir el archivo de audio (en formato WAV)
audio_file = "ruta_del_archivo_de_audio.wav"
with sr.AudioFile(audio_file) as source:
    # Leer el audio del archivo
    audio = r.record(source)

    try:
        # Utilizar el reconocedor para convertir el habla a texto
        text = r.recognize_google(audio, language="es-ES")  # Puedes ajustar el idioma según tus necesidades
        print("Texto reconocido:")
        print(text)
        
        
    except sr.UnknownValueError:
        print("No se pudo reconocer el habla")
        
        
    except sr.RequestError as e:
        print(f"Error al realizar la solicitud: {e}")


