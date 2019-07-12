import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load('es_core_news_sm')
ruler = EntityRuler(nlp)
patterns = [{"label": "gano", "pattern": "gano"},
            {"label": "gano", "pattern": "ganó"},
            {"label": "gano", "pattern": "pasó"},
            {"label": "gano", "pattern": "aprobó"},
            {"label": "perdio", "pattern": "perdio"},
            {"label": "perdio", "pattern": "perdió"},
            {"label": "perdio", "pattern": "reprobó"},
            {"label": "perdio", "pattern": "reprobo"},
            {"label": "perdio", "pattern": [{"lower": "no"}, {"lower": "ganó"}]},
            {"label": "perdio", "pattern": [{"lower": "no"}, {"lower": "aprobó"}]},
            {"label": "perdio", "pattern": [{"lower": "no"}, {"lower": "pasó"}]}]

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)

def posiblesVerbos(text):
    doc = nlp(text)
    entidades = []
    for ent in doc.ents:
      entidades.append( ent.label_)