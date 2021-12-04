import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

mensaje='Hola, esta es una prueba de voz con Python. Saludos'

engine.say(mensaje)

mensaje='12345.67'

engine.say(mensaje)
#engine.save_to_file(mensaje,'mensaje.mp3')
engine.runAndWait()
