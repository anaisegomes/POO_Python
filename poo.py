class Pessoa: 
    def __init__(self, nome, idade):   # __init__ é o construtor, chamado quando o objeto é criado
        self.nome = nome  # self referencia a própria instancia
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")


p1 = Pessoa("Julia", 25)
p2 = Pessoa("Karlos", 30)

p1.apresentar()
p2.apresentar()
        