import spacy    
from spacy.pipeline import EntityRuler
from model import posiblesTablas, EscucharVoz, posiblesPronombres, posiblesSustantivos, posiblesTablas2, devuelveColeccion
from modelo2 import posiblesPreguntas
from atributos import posiblesAtributos
from reproducir import hablar


nlp = spacy.load('es_core_news_sm')
 
def devolverNotas(alumno, notas, coleccion):
    frase = ''
    frases = []
    for estudiante in coleccion:
        if(alumno == estudiante['nombre']):
            frase = alumno + " tiene las siguientes notas: "
            for nota in notas:
                if(nota in estudiante.keys()):
                    frase = frase  + nota + ": " + str(estudiante[nota]) + "    "
    return frase



def imprimirFrase1(nombre, texto):
    print("las notas de {} son ".format(nombre) +texto)


if __name__ == "__main__":
    text = EscucharVoz() 
    # text = 'cuáles todas de Gustavo y Héctor de compiladores'
    text2 = text.lower()
    doc = nlp(text)
    print(text)
    tablas = posiblesTablas(text2)
    pregunta = posiblesPreguntas(text2)
    pron = posiblesPronombres(text)
    nouns = posiblesAtributos(text)
    if(len(tablas) == 1):
        col = devuelveColeccion(tablas[0])
        if(pregunta[0] == 'cual'):
            for nombres in pron:
                n = devolverNotas(nombres, nouns, col)
                if(n != ''):
                    hablar(n)
                print(n)

        if(pregunta[0] == 'quien'):
            pass
                


    
