person = {
		"jorge@teste.com": {"nome": "Jorge", "idade": 24},
		"thamyres@teste.com": {"nome": "Thamyres", "idade": 26},
		"sogro@teste.com": {"nome": "Marcos", "idade": 50},
		"sogra@teste.com": {"nome": "Tanyr", "idade": 48, "extra": {"a":"sorte grande"}},

}

chamada = person["sogra@teste.com"]["nome"] # "Tanyr"
print(chamada)

new_chamada = person["sogra@teste.com"]
print(new_chamada)


for chave, valor in person.items():
    print(chave, valor)

	
