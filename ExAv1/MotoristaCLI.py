from classesBD import Motorista, Corridas, Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nota = int(input("Entre com a nota do motorista: "))
        corridas = []
        while True:
            add_corrida = input("Adicionar outra corrida? (sim ou nao): ")
            if add_corrida.lower() == "nao":
                break
            nota_corrida = int(input("Entre com a nota da corrida: "))
            distancia_corrida = float(input("Entre com a distancia da corrida: "))
            valor_corrida = float(input("Entre com o valor da corrida: "))
            nome_passageiro = input("Entre com o nome do passageiro: ")
            documento_passageiro = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corridas(nota_corrida, distancia_corrida, valor_corrida, passageiro)
            corridas.append(corrida)
        self.motorista_model.create_motorista(nota, corridas)

    def read_motorista(self):
        id = input("Entre com o id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            print(f"Nota: {motorista.nota}")
            print("Corridas:")
            for corrida in motorista.corridas:
                print(f"Nota: {corrida.nota}")
                print(f"Distancia: {corrida.distancia}")
                print(f"Valor: {corrida.valor}")
                print(f"Nome do passageiro: {corrida.passageiro.nome}")
                print(f"Documento do passageiro: {corrida.passageiro.documento}")

    def update_motorista(self):
        id = input("Entre com o id: ")
        nota = int(input("Entre com a nova nota (1-5): "))
        corrida_nota = int(input("Entre com a nova nota da corrida (1-5): "))
        distancia = float(input("Entre com a nova distancia da corrida: "))
        valor = float(input("Entre com o novo valor da corrida: "))
        nome = input("Entre com o novo nome do passageiro: ")
        documento = input("Entre com o novo documento do passageiro: ")
        passageiro = Passageiro(nome, documento)
        corrida = Corridas(corrida_nota, distancia, valor, passageiro)
        self.motorista_model.update_motorista(id, nota, corrida)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()