#!/usr/bin/env python
# -*- coding: utf-8 -*-
import spacy
from spacy.lang.es.examples import sentences
from spacy.pipeline import EntityRuler
from model import *

nlp = spacy.load('es_core_news_sm')


