from database import Database
from livroModel import LivroModel
from cli import LivroCLI
from writeAJson import writeAJson

db = Database(database="Relatorio5", collection="Livros")
livroModel = LivroModel(database=db)

livroCLI = LivroCLI(livroModel)
livroCLI.run()