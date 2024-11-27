def conta_vogais(texto):
    vogais = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    contador = 0

    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

texto = input()
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")