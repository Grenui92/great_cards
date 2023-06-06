import pyttsx3

en_sound_engine = pyttsx3.init()
en_sound_engine.setProperty('rate', 150)
en_sound_engine.setProperty('voice', 'english')

ru_sound_engine = pyttsx3.init()
ru_sound_engine.setProperty('rate', 100)
ru_sound_engine.setProperty('voice', 'russian')

