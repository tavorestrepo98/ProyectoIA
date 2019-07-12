import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load('es_core_news_sm')
ruler = EntityRuler(nlp)
patterns = [{"label": "cual", "pattern": "cuál"},  
            {"label": "cual", "pattern": "cual"},
            {"label": "cual", "pattern": [{"lower": "cuál"}, {"lower": "es"}]},
            {"label": "cual", "pattern": [{"lower": "cual"}, {"lower": "es"}]},
            {"label": "cual", "pattern": "Cuáles"},
            {"label": "cual", "pattern": "Cuales"},
            {"label": "cual", "pattern": [{"lower": "cuáles"}, {"lower": "son"}]},
            {"label": "cual", "pattern": [{"lower": "cuales"}, {"lower": "son"}]},
            {"label": "cual", "pattern": [{"lower": "digame"}, {"lower": "la"}]},
            {"label": "cual", "pattern": [{"lower": "digame"}, {"lower": "las"}]},
            {"label": "cual", "pattern": [{"lower": "dígame"}, {"lower": "la"}]},
            {"label": "cual", "pattern": [{"lower": "dígame"}, {"lower": "las"}]},
            {"label": "cual", "pattern": "muéstreme"},
            {"label": "cual", "pattern": "muéstrame"},
            {"label": "quien", "pattern": "quien"},
            {"label": "quien", "pattern": "quién"},
            {"label": "quien", "pattern": "Quien"},
            {"label": "quien", "pattern": "Quién"},
            {"label": "quien", "pattern": "Quienes"},
            {"label": "quien", "pattern": "quienes"}]

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)

# Esta funcion ddevuelve las posibles preguntas que se encuentren en la frase
def posiblesPreguntas(text):
    doc = nlp(text)
    entidades = []
    for ent in doc.ents:
      entidades.append(ent.label_)

    return entidades