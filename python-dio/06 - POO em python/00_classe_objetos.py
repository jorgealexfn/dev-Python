class cachorro:
	def __init__(self, nome, cor, acordado=True):
		self.nome = nome
		self.cor = cor
		self.acordado = acordado
		
	def latir(self):
		print("AUAUAU")
	
	def dormir(self):
		self.acordado = False
		print("ZZzzzzz...")
		
cao_1 = cachorro("Chappie","Amarelo", False)
cao_2 = cachorro("Aladim","Branco e preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)