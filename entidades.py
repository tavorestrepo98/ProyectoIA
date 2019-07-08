import spacy    
from spacy.pipeline import EntityRuler
from model import posiblesTablas, EscucharVoz
from modelo2 import posiblesPreguntas

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


text = EscucharVoz() 
text = text.lower()

doc = nlp(text)

print(posiblesTablas(text))
print(posiblesPreguntas(text))
print(doc.text)