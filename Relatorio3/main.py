from database import Database
from helper.WriteAJson import writeAJson
from pokedex import Pokedex

#db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()
#pokemon = db.collection.find_one({"name": "Mewtwo"})
#writeAJson(pokemon, "pokemon")

pokemon = "Pikachu"
type = ["Fire", "Flying"]
not_type = ["Bug", "Rock"]
evoByType = ["Water", "Grass"]
typeNoEvo = ["Water", "Grass", "Fire", "Flying", "Bug", "Rock"]
noEggByType = ["Dragon", "Ice"]
eeveelutionType = ["Electric", "Water"]

Pokedex.getPokemonByName(pokemon)
Pokedex.getPokemonByType(type)
Pokedex.notType(not_type)
Pokedex.evoByType(evoByType)
Pokedex.noEvoByType(typeNoEvo)
Pokedex.noEggByType(noEggByType)
Pokedex.eeveelutionsByType(eeveelutionType)


