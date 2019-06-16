#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spacy
from spacy.lang.es.examples import sentences

import speech_recognition as sr
r = sr.Recognizer()

nlp = spacy.load('es_core_news_sm')

with sr.Microphone() as source:
    print('Say something')
    audio = r.listen(source, phrase_time_limit=6)
    print('TIME OVER, THANKS')

try: 
    text = r.recognize_google(audio, language='es_ES')
    print('TEXT ' + text)
except:
    print('no funciona')

doc = nlp(text)
    
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

