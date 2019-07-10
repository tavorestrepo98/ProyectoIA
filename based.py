#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo as pm

client = pm.MongoClient('localhost', 27017)
db = client.proyectoia

def coleccion(nombre):
    alumnos = []
    col = db[nombre]
    for alumno in col:
        alumnos.append(alumno)
    return alumnos