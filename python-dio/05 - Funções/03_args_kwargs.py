def exibir_poema(data_extenso, *lista, **dicionario):
	texto = "\n".join(lista)
	meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
	
	mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
	print(mensagem)
	
exibir_poema(
	"Sexta-feira, 26 de Agosto de 2024",
	"Zen of python",
	"Beautiful is better than ugly.",
	autor="Tim Petters",
	ano=1999
 )