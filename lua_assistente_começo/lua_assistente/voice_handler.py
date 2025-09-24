from gtts import gTTS
import os
import pygame
import time
import speech_recognition as sr
import uuid

def speak(texto):
    tts = gTTS(text=texto, lang='pt-br')
    filename = f"tmp_{uuid.uuid4().hex}.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    os.remove(filename)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        audio = r.listen(mic)
    try:
        return r.recognize_google(audio, language="pt-BR").lower()
    except:
        return ""