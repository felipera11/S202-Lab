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


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_model):
        super().__init__()
        self.teacher_model = teacher_model
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input("Enter teacher name: ")
        ano_nasc = input("Enter teacher ano_nasc: ")
        cpf = input("Enter teacher cpf: ")
        self.teacher_model.create(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Enter teacher name: ")
        print(self.teacher_model.read(name))

    def update_teacher(self):
        name = input("Enter teacher name: ")
        newCpf = input("Enter new teacher cpf: ")
        self.teacher_model.update(name, newCpf)

    def delete_teacher(self):
        name = input("Enter teacher name: ")
        self.teacher_model.delete(name)

    def run(self):
        print("Welcome to the Teacher CLI!")
        print("Available commands: {}".format(list(self.commands.keys())))
        super().run()