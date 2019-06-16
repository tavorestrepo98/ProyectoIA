#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import pyworld as pw
from gtts import gTTS
from tempfile import TemporaryFile
from pygame import mixer
import spacy
from spacy.lang.es.examples import sentences
import speech_recognition as sr


r = sr.Recognizer()
ficheromp3 = 'C:\\Users\\tavor\\OneDrive\\Escritorio\\ProyectoIA\\tts.mp3'

nlp = spacy.load('es_core_news_sm')

with sr.Microphone() as source:
    print('Say something')
    audio = r.listen(source, phrase_time_limit=4)
    print('TIME OVER, THANKS')

try: 
    text = r.recognize_google(audio, language='es-Es')
    print('TEXT ' + text)
except:
    text = 'no funciona'
    print(text)

doc = nlp(text)
tts = gTTS(text=text, lang="es")
    
for token in doc:
    print(token, token.pos_, token.dep_)



tts.save(ficheromp3)
mixer.init()
mixer.music.load(ficheromp3)
print("Reproduciendo {0}".format(ficheromp3))
mixer.music.play()
while mixer.music.get_busy():
    pygame.time.Clock().tick(10)
mixer.quit()

