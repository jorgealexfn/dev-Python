class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

# Entrada do usuário
nome = input("")
idade = int(input(""))

# Criando uma instância da pessoa
pessoa = Pessoa(nome, idade)

# Imprimindo a pessoa diretamente
print(pessoa)