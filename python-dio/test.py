def conta_vogais(texto):
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    contador1 = 0

    for caractere in texto:
        if caractere in vogais:
            contador1 += 1
    return contador1

def conta_consoante(texto):
    consoante = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"}

    contador = 0

    for caractere in texto:
        if caractere in consoante:
            contador += 1
    return contador

texto = input("Digite o que voce deseja contar Vogais, Consoantes e quandidade de letras no total :")
resultado = conta_vogais(texto)
resultado1 = conta_consoante(texto)
print(f"O número de vogais e consoante na string '{texto}' é: Vogais : {resultado} , Consoante: {resultado1} e total de letras: {len(texto)}")