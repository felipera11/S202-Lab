class Query:
    def __init__(self, database):
      self.db = database
      
    def get_renzo_data(self):
      query = "MATCH (t:Teacher) WHERE t.name = 'Renzo' RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
      results = self.db.execute_query(query)
      return [(result["ano_nasc"], result["cpf"]) for result in results]
    
    def get_name_start_m(self):
      query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
      results = self.db.execute_query(query)
      return [(result["name"], result["cpf"]) for result in results]
    
    def get_all_cities(self):
      query = "MATCH (c:City) RETURN c.name AS names"
      results = self.db.execute_query(query)
      return [result["names"] for result in results]
    
    def get_schools_info(self):
      query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <= 550 RETURN s.name AS name, s.address AS address, s.number AS number"
      results = self.db.execute_query(query)
      return [(result["name"], result["address"], result["number"]) for result in results]
    
    def get_year_younger_older_teacher(self):
      query = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS younger, MIN(t.ano_nasc) AS older"
      results = self.db.execute_query(query)
      return [(result["younger"], result["older"]) for result in results]
    
    def get_avg_population(self):
      query = "MATCH (c:City) RETURN AVG(c.population) AS avg_population"
      results = self.db.execute_query(query)
      return [result["avg_population"] for result in results]
    
    def get_cep_srs(self):
      query = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN REPLACE(c.name, 'a', 'A') AS new_name"
      results = self.db.execute_query(query)
      return [result["new_name"] for result in results]

    def teacher(self):
      query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2, 1) AS characther"
      results = self.db.execute_query(query)
      return [result["characther"] for result in results]