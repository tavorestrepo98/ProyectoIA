import spacy    
from spacy.pipeline import EntityRuler
from model import posiblesTablas, EscucharVoz, posiblesPronombres, posiblesSustantivos, posiblesTablas2, coleccion
from modelo2 import posiblesPreguntas


nlp = spacy.load('es_core_news_sm')
 
# text = EscucharVoz() 
text = 'me gusta ir a compiladores'
text2 = text.lower()

doc = nlp(text)

print(posiblesTablas(text)[0][1]) #tablas las cuales nos van a preguntar
print(posiblesPreguntas(text2)) #cómo nos vana a preguntar
print(posiblesPronombres(text)) #nombres de los estudiantes si los hay
print(posiblesSustantivos(text))
print(doc.text)
print(coleccion(posiblesTablas(text)[0][1]))


