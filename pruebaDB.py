from peewee import *
from datetime import date

db = SqliteDatabase('alumnos.db')

class Person(Model):
    name = CharField();
    birthday = DateField();

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

db.connect()

db.create_tables([Person, Pet])

def addPerson(nombre, ano, mes, dia):
    persona = Person(name = nombre, birthday = date(ano, mes, dia))
    persona.save()



if __name__ == "__main__":
    nombre = input('nombre: ')
    ano = int(input('año: '))

    addPerson(nombre, ano, 7, 12)
