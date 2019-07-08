#!/usr/bin/env python
# -*- coding: utf-8 -*-
import spacy
from spacy.lang.es.examples import sentences
# from spacy_lookup import Entity
from spacy.pipeline import EntityRuler
from model import *
# from reproducir import hablar

nlp = spacy.load('es_core_news_sm')

text = EscucharVoz()
 
doc = nlp(text)


for token in doc:
    print(token.text, " ## ", token.lemma_," ## ", token.pos_," ## ", token.tag_," ## ", token.dep_," ## ",
            token.shape_," ## ", token.is_alpha," ## ", token.is_stop)






