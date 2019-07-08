import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load('es_core_news_sm')
ruler = EntityRuler(nlp)
patterns = [{"label": "cual", "pattern": "cuál"},
            {"label": "cual", "pattern": [{"lower": "cuál"}, {"lower": "es"}]},
            {"label": "cual", "pattern": "Cuáles"},
            {"label": "cual", "pattern": [{"lower": "cuáles"}, {"lower": "son"}]},
            {"label": "cual", "pattern": [{"lower": "digame"}, {"lower": "la"}]}]

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)

# Esta funcion ddevuelve las posibles preguntas que se encuentren en la frase
def posiblesPreguntas(text):
    doc = nlp(text)
    entidades = []
    for ent in doc.ents:
      entidades.append((ent.text, ent.label_))

    return entidades