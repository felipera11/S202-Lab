from database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")


class Pokedex:

    def getPokemonByName(name: str):
        try:
            name_search = db.collection.find({"name": name})
            writeAJson(name_search, "name_search")
            print("Query getPokemonByName realizado com sucesso!")
        except Exception as e:
            print(e)

    def getPokemonByType(type: list):
        try:
            type_search = db.collection.find({"type": {"$in": type}})
            writeAJson(type_search, "type_search")
            print("Query getPokemonByType realizado com sucesso!")
        except Exception as e:
            print(e)

    def notType(type: list):
        try:
            not_type_search = db.collection.find({"type": {"$nin": type}})
            writeAJson(not_type_search, "not_type_search")
            print("Query notType realizado encontrado com sucesso!")
        except Exception as e:
            print(e)

    def evoByType(type: list):
        try:
            evo_by_type = db.collection.find({"type": {"$in": type}, "next_evolution": {"$exists": True}})
            writeAJson(evo_by_type, "evo_by_type")
            print("Query evoByType realizado com sucesso!")
        except Exception as e:
            print(e)

    def noEvoByType(type: list):
        try:
            no_evo_by_type = db.collection.find({"type": {"$in": type}, "next_evolution": {"$exists": False}, "prev_evolution": {"$exists": False}})
            writeAJson(no_evo_by_type, "no_evo_by_type")
            print("Query noEvoByType realizado com sucesso!")
        except Exception as e:
            print(e)

    def noEggByType(type: list):
        try:
            no_egg_by_type = db.collection.find({"type": {"$in": type}, "egg": "Not in Eggs"})
            writeAJson(no_egg_by_type, "no_egg_by_type")
            print("Query noEggByType realizado com sucesso!")
        except Exception as e:
            print(e)

    def eeveelutionsByType(type: list):
        try:
            eeveelutions_by_type = db.collection.find({"type": {"$in": type}, "prev_evolution.name": "Eevee"})
            writeAJson(eeveelutions_by_type, "eeveelutions_by_type")
            print("Query eeveelutionsByType realizado com sucesso!")
        except Exception as e:
            print(e)