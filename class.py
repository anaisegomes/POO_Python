class Usuario:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greetings(self):
        print(f"Usuário: {self.name}, idade: {self.age}")

Usuario1 = Usuario(name='Fernanda', age=24)
Usuario1.greetings()

print(Usuario1)