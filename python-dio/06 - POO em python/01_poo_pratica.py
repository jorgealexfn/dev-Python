class bicicleta :
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = int(ano)
        self.valor = float(valor)
    
    def buzinar(self):
        print("BIIIIIIIIIIIIIIIIIIIIII")
    
    def freiar(self):
        print("Apertando os freios...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Acelerando...")

bicicleta_1 = bicicleta("preto", "caloi", 2015, 780.00)
bicicleta_2 = bicicleta("vermelho", "caloi", 2024, 1599.99)

escolha = ()

escolha = int(input("Escolha qual bicicleta vamos testar: \n[1] - caloi 2015 \n[2] - caloi 2024\n[3] - Só dando uma olhadinha\n --> "))

if escolha == 1:
    bicicleta_1.buzinar()
    bicicleta_1.correr()
    bicicleta_1.freiar()

    print(f"O valor da bicicleta está: R${bicicleta_1.valor}")
elif escolha ==2:
    bicicleta_2.buzinar()
    bicicleta_2.correr()
    bicicleta_2.freiar()

    print(f"O valor da bicicleta está: R${bicicleta_2.valor}")

else:
    print("!TA DURO DORME!")


        
