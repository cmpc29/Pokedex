import sqlite3
from functions import catch

connect = sqlite3.connect("Pokedex.db")
cursor = connect.cursor()

class Pokemon:
    def __init__(self,species,type1=None,type2=None,description=None,height=None,weight=None,category=None,ability=None):
        self.species=species
        self.type1=type1
        self.type2=type2
        self.description=description
        self.height=height
        self.weight=weight
        self.category=category
        self.ability=ability

name=input().upper()
name=name[0].upper()+name[1:].lower()
pokemon=Pokemon(name)

catch(pokemon)

