#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spacy
from spacy.lang.es.examples import sentences 

texto = 'muestre las notas de los parciales de Gustavo Restrepo, luego saque el promedio'

nlp = spacy.load('es_core_news_md')
doc = nlp(texto)

for token in doc:
    print(token.text, token.pos_, token.dep_)

print("sustantivos:", [token.text for token in doc if token.pos_ == "NOUN"])
print("Verbos:", [token.text for token in doc if token.pos_ == "VERB"])