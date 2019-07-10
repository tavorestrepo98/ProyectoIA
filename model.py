import spacy
import speech_recognition as sr
from spacy.pipeline import EntityRuler
import pymongo as pm

client = pm.MongoClient('localhost', 27017)
db = client.proyectoia

nlp = spacy.load('es_core_news_sm')
ruler = EntityRuler(nlp)
patterns = [{"label": "ia", "pattern": "ia"},
            {"label": "ia", "pattern": "ai"},
            {"label": "compiladores", "pattern": "compiladores"},
            {"label": "compiladores", "pattern": "compi"},
            {"label": "compiladores", "pattern": "compilador"},
            {"label": "comunicaciones", "pattern": "comunicaciones"},
            {"label": "comunicaciones", "pattern": "comu"},
            {"label": "comunicaciones", "pattern": "comunicamierda"},
            {"label": "ia", "pattern": [{"lower": "Inteligencia"}, {"lower": "artificial"}]},
            {"label": "ia", "pattern": [{"lower": "inteligencia"}, {"lower": "artificial"}]},
            {"label": "ia", "pattern": [{"lower": "artificial"}, {"lower": "intelligence"}]}]

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)

r = sr.Recognizer()

def EscucharVoz():
    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source, phrase_time_limit=6)
        print('TIME OVER, THANKS')
    try: 
        text = r.recognize_google(audio, language='es-CO')
    except:
        text = 'no funciona el reconocimiento de voz'
        print(text)
    return text 


# Esta funcion ddevuelve las posibles tablas a las que voy hacer consulta en la base de datos
def posiblesTablas(text):
    doc = nlp(text)
    entidades = []
    for ent in doc.ents:
      entidades.append((ent.text, ent.label_))

    return entidades

def posiblesTablas2(text):
    doc = nlp(text)
    entidades = []
    for ent in doc.ents:
      entidades.append(ent.label)

    return entidades

def posiblesPronombres(text):
    doc = nlp(text)
    pronombres = []
    for token in doc:
        if (token.pos_ == "PROPN"):
            pronombres.append((token.text, token.pos_))
        
    return pronombres

def posiblesSustantivos(text):
    doc = nlp(text)
    sustantivos = []
    for token in doc:
        if (token.pos_ == "NOUN"):
            sustantivos.append((token.text, token.pos_))
        
    return sustantivos



def coleccion(nombre):
    alumnos = []
    col = db[nombre]
    cursor = col.find()
    for alumno in cursor:
        alumnos.append(alumno)
    return alumnos