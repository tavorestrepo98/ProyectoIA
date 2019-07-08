#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import pyworld as pw
from gtts import gTTS
from tempfile import TemporaryFile
from pygame import mixer

ficheromp3 = 'C:\\Users\\tavor\\OneDrive\\Escritorio\\ProyectoIA\\tts.mp3'


def hablar(texto):
    tts = gTTS(text=texto, lang="es")
    tts.save(ficheromp3)
    mixer.init()
    mixer.music.load(ficheromp3)
    print("Reproduciendo {0}".format(ficheromp3))
    mixer.music.play()
    while mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    mixer.quit()