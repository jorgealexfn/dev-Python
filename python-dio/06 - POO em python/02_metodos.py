class Cachorro:
    def __init__(self, nome, cor, acordado= True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia")

    def falar(self):
        print("auauauauaua")

c = Cachorro("bolinha", "amarelo")
c.falar()
