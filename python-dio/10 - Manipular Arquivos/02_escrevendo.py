file = open("D:\\dev Python\\python-dio\\10 - Manipular Arquivos\\teste.txt", "w")

file.write("Escrevendo dados em um novo arquivo, vulgo container... saca ??")
file.writelines(["\nEscrevendo", "\num", "\nnovo", "\nTexto"])

file.close()