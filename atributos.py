import spacy
from spacy.pipeline import EntityRuler

nlp = spacy.load('es_core_news_sm')
ruler = EntityRuler(nlp)
patterns = [{"label": "nota1", "pattern": "nota1"},
            {"label": "nota1", "pattern": [{"lower": "nota"}, {"lower": "uno"}]},
            {"label": "nota1", "pattern": [{"lower": "nota"}, {"lower": "1"}]},
            {"label": "nota1", "pattern": [{"lower": "parcial"}, {"lower": "uno"}]},
            {"label": "nota1", "pattern": [{"lower": "primera"}, {"lower": "nota"}]},
            {"label": "nota1", "pattern": [{"lower": "primer"}, {"lower": "corte"}]},
            {"label": "nota1", "pattern": [{"lower": "primer"}, {"lower": "parcial"}]},
            {"label": "nota1", "pattern": [{"lower": "primer"}, {"lower": "examen"}]},
            {"label": "nota1", "pattern": [{"lower": "examen"}, {"lower": "uno"}]},
            {"label": "nota2", "pattern": "nota2"},
            {"label": "nota2", "pattern": [{"lower": "nota"}, {"lower": "dos"}]},
            {"label": "nota2", "pattern": [{"lower": "nota"}, {"lower": "2"}]},
            {"label": "nota2", "pattern": [{"lower": "parcial"}, {"lower": "dos"}]},
            {"label": "nota2", "pattern": [{"lower": "segunda"}, {"lower": "nota"}]},
            {"label": "nota2", "pattern": [{"lower": "segundo"}, {"lower": "corte"}]},
            {"label": "nota2", "pattern": [{"lower": "segundo"}, {"lower": "parcial"}]},
            {"label": "nota2", "pattern": [{"lower": "segundo"}, {"lower": "examen"}]},
            {"label": "nota3", "pattern": "nota3"},
            {"label": "nota3", "pattern": [{"lower": "nota"}, {"lower": "tres"}]},
            {"label": "nota3", "pattern": [{"lower": "nota"}, {"lower": "3"}]},
            {"label": "nota3", "pattern": [{"lower": "parcial"}, {"lower": "tres"}]},
            {"label": "nota3", "pattern": [{"lower": "tercera"}, {"lower": "nota"}]},
            {"label": "nota3", "pattern": [{"lower": "tercer"}, {"lower": "corte"}]},
            {"label": "nota3", "pattern": [{"lower": "tercer"}, {"lower": "parcial"}]},
            {"label": "nota3", "pattern": [{"lower": "tercer"}, {"lower": "examen"}]},
            {"label": "todo", "pattern": [{"lower": "todas"}, {"lower": "las"}, {"lower": "notas"}]},
            {"label": "todo", "pattern": [{"lower": "las"}, {"lower": "notas"}]}]

ruler.add_patterns(patterns)
nlp.add_pipe(ruler)

def posiblesAtributos(text):
    doc = nlp(text)
    entidades = []
    for ent in doc.ents:
      entidades.append(ent.label_)
    if('todo' in entidades):
      return ['nota1', 'nota2', 'nota3']
    return entidades