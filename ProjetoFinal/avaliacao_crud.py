class AvaliacaoCRUD:
    def __init__(self, database):
        self.db = database

    def create_person(self, name, idade, sexo):
        query = "CREATE (:Pessoa {name: $name, idade: $idade, sexo: $sexo})"
        parameters = {"name": name, "idade": idade, "sexo": sexo}
        self.db.execute_query(query, parameters)

    def create_movie(self, name, ano_lanc, diretor, genero):
        query = "CREATE (:Filme {name: $name, ano_lanc: $ano_lanc, diretor: $diretor, genero: $genero})"
        parameters = {"name": name, "ano_lanc": ano_lanc, "diretor": diretor, "genero": genero}
        self.db.execute_query(query, parameters)

    def create_aval(self, name_pessoa, name_filme, nota, comentario):
        query = "MATCH (p:Pessoa {name: $name_pessoa}), (f:Filme {name: $name_filme}) CREATE (p)-[:AVALIOU {nota: $nota, comentario: $comentario}]->(f)"
        parameters = {"name_pessoa": name_pessoa, "name_filme": name_filme, "nota": nota, "comentario": comentario}
        self.db.execute_query(query, parameters)


    def update_aval(self, name_pessoa, name_filme, newNota, newComentario):
        query = "MATCH (p:Pessoa {name: $name_pessoa})-[a:AVALIOU]->(f:Filme {name: $name_filme}) SET a.nota = $newNota, a.comentario = $newComentario"
        parameters = {"name_pessoa": name_pessoa, "name_filme": name_filme, "newNota": newNota, "newComentario": newComentario}
        self.db.execute_query(query, parameters)

    
    def read_person(self, name):
        query = "MATCH (p:Pessoa {name: $name}) RETURN p AS pessoa_name"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["pessoa_name"] for result in results]
    
    def read_movie(self, name):
        query = "MATCH (f:Filme {name: $name}) RETURN f AS filme_name"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["filme_name"] for result in results]
    
    def read_aval(self, name, movie):
        query = "MATCH (p:Pessoa {name: $name})-[a:AVALIOU]->(f:Filme {movie: $movie}) RETURN a AS aval_name"
        parameters = {"name": name, "movie": movie}
        results = self.db.execute_query(query, parameters)
        return [result["aval_name"] for result in results]
    


    def delete_movie(self, name):
        query = "MATCH (f:Filme {name: $name}) DETACH DELETE f"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_person(self, name):
        query = "MATCH (p:Pessoa {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_aval(self, name_pessoa, name_movie):
        query = "MATCH (p:Pessoa {name: $name_pessoa})-[a:AVALIOU]->(f:Filme {name: $name_movie}) DELETE a"
        parameters = {"name_pessoa": name_pessoa, "name_movie": name_movie}
        self.db.execute_query(query, parameters)
