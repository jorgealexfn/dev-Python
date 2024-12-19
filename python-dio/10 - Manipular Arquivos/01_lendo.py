file = open("D:\\dev Python\\python-dio\\10 - Manipular Arquivos\\dados.txt", "r")
#print(file.readline())

# for line in file.readlines():
#     print(line)

while len(line := file.readline()) :
    print( line)

file.close()