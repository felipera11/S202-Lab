from pymongo import MongoClient
from bson.objectid import ObjectId
from classesBD import Motorista, Corridas, Passageiro

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, nota: int, corridas: list):
        corridas_dict = []
        for corrida in corridas:
            corrida_dict = {
                "nota": corrida.nota,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro": {
                    "nome": corrida.passageiro.nome,
                    "documento": corrida.passageiro.documento
                }
            }
            corridas_dict.append(corrida_dict)

        try:
            res = self.db.collection.insert_one({
                "nota": nota,
                "corridas": corridas_dict
            })
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            motorista_dict = self.db.collection.find_one({"_id": ObjectId(id)})
            if(motorista_dict):
                notas = motorista_dict['nota_motorista']
                corridas_dict = motorista_dict['corridas']
                corridas = [Corridas(corrida_dict['nota_corrida'], corrida_dict['distancia'], corrida_dict['preco'], 
                                     Passageiro(corrida_dict['passageiro']['nome'], corrida_dict['passageiro']['documento'])) for corrida_dict in corridas_dict]
            print(f"Motorista found: {motorista_dict}")
            return Motorista(notas, corridas)
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, id: str, nota: int, corridas: list):
        corridas_dict = []
        for corrida in corridas:
            corrida_dict = {
                "nota": corrida.nota,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro": {
                    "nome": corrida.passageiro.nome,
                    "documento": corrida.passageiro.documento
                }
            }
            corridas_dict.append(corrida_dict)

        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": nota, "corridas": corridas_dict}})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletado(s)")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return
