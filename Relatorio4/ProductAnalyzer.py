from database import Database
from helper.WriteAJson import writeAJson

db = Database(database="mercado", collection="compras")


class productAnalyzer:

    def totalVendasPorDia():
        try:
            result = db.collection.aggregate([
                {"$unwind": "$produtos"},
                {"$group": {"_id": "$data_compra", "total": {
                    "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
                {"$sort": {"_id": 1}}
            ])
            writeAJson(result, "Total de vendas")
            print("Query totalVendas realizado com sucesso!")
        except Exception as e:
            print(e)

    def produtoMaisVendido():
        try:
            result = db.collection.aggregate([
                {"$unwind": "$produtos"},
                {"$group": {"_id": "$produtos.descricao",
                            "total": {"$sum": "$produtos.quantidade"}}},
                {"$sort": {"total": -1}},
                {"$limit": 1}
            ])
            writeAJson(result, "Produto mais vendido")
            print("Query produto mais vendido realizado com sucesso!")
        except Exception as e:
            print(e)

    def clienteQueMaisComprou():
        try:
            result = db.collection.aggregate([
                {"$unwind": "$produtos"},
                {"$group": {"_id": "$cliente_id", "total": {
                    "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
                {"$sort": {"total": -1}},
                {"$limit": 1}
            ])
            writeAJson(result, "Cliente mais gastao")
            print("Query cliente mais gastao realizado com sucesso!")
        except Exception as e:
            print(e)

    def produtoAcima1():
        try:
            result = db.collection.aggregate([
                {"$unwind": "$produtos"},
                {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
                {"$sort": {"total": -1}},
                {"$match": {"total": {"$gt": 1}}}
            ])
            writeAJson(result, "Produto acima de 1")
            print("Query produto acima de 1 realizado com sucesso!")
        except Exception as e:
            print(e)