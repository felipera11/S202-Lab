class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento


class Corridas:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro


class Motorista:
    def __init__(self, nota: int, corridas: list[Corridas]):
        self.nota = nota
        self.corridas = corridas