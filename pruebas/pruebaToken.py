#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spacy
from spacy.lang.es.examples import sentences 

nlp = spacy.load('es_core_news_sm')
doc = nlp('Hola mi amor, te quiero mucho')
print(doc.text)

print(doc.noun_chunks)

for token in doc:
    print(token.text, token.pos_, token.dep_)