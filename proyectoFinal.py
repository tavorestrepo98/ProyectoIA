import spacy
nouns = []
POS = {}

head_text = {}

nlp = spacy.load('es')

# # Process a text
# doc = nlp("Ella comió pizza")

# # Iterate over the tokens
# for token in doc:
#     # Print the text and the predicted part-of-speech tag
#     print(token.text, token.pos_, token.dep_,token.head.text)
# spacy.explain('etiqueta') De aqui se obtiene una explicacion rapida de las etiquetas
# doc = nlp("De que color es el carro de Héctor")
# for token in doc:
#     print(token.text, token.pos_, token.dep_, token.head.text)
# for ent in doc.ents:
#     print(ent.text, ent.label_)

doc = nlp("De que color es el carro de Hector")


def getPOSdoc(doc):
    for token in doc:
        if token.pos_ in POS:
            POS[token.pos_].append(token.text)
        else:  
            POS[token.pos_] = []
            POS[token.pos_].append(token.text)

getPOSdoc(doc)

def getPredominantNoun(doc):
    global POS
    for token in doc:
        if token.text == token.head.text:
            return token.text

for token in doc:
    print("Token {}, POS {}, dependencia {}, principal {}".format(token.text, token.pos_, token.dep_, token.head.text))


print(POS)
table = getPredominantNoun(doc)

print("SELECT * FROM {} WHERE dueño={}".format(table,POS['PROPN'][0]))

# for chunk in doc.noun_chunks:
#     print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)