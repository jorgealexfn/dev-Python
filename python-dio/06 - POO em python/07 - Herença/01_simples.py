class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(".....Ligando o motor..... ")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'sim' if self.carregado else 'nao'} estou carregado")
        

moto = Motocicleta("vermela", "DIO-666", 2)
moto.ligar_motor()

carro = Carro("Branco", "COE-171", 4)
carro.ligar_motor()

caminhao = Caminhao("preto", "XXG - 9999", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()

