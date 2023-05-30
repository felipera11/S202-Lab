from database import Database
from query import Query
from teacher_crud import TeacherCRUD
from cli import TeacherCLI

db=Database("bolt://localhost:7687", "neo4j", "password")

get_db = Query(db)
cli_db = TeacherCRUD(db)

#questao 1
print("Dados do professor Renzo"+str(get_db.get_renzo_data()))

print("Professores que começam com M"+str(get_db.get_name_start_m()))

print("Todas as cidades"+str(get_db.get_all_cities()))

print("Escolas com número entre 150 e 550"+str(get_db.get_schools_info()))

#questao 2

print("Professor mais velho e mais novo"+str(get_db.get_year_younger_older_teacher()))

print("Média da população"+str(get_db.get_avg_population()))

print("Cidades com cep 37540-000"+str(get_db.get_cep_srs()))

print("3 letra do nome dos professores"+str(get_db.get_teacher_letter()))

#questao 3

cli_db.create("Chris Lima", 1956, "189.052.396-66")
cli_db.update("Chris Lima", "162.052.777-77")
print(str(cli_db.read("Chris Lima")))

teachercli = TeacherCLI(cli_db)
teachercli.run()

db.close()
