import random

def jogo_forca():
    palavras = ["python", "progamacao", "computador", "algoritmo"]
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ["_" for letra in palavra_secreta]
    tentativas = 6

    while tentativas > 0:
        print(" ".join(letras_acertadas))
        chute = input("Chute uma letra: ").lower()

        if chute in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == chute:
                    letras_acertadas[i] = chute
        else:
            tentativas -= 1
            print(f"A letra \"{chute}\" não existe na palavra.")
        if "_" not in letras_acertadas:
            print("Parabéns, você venceu!")
            break
    if "_" in letras_acertadas:
        print("Voce perdeu! A palavra era: ", palavra_secreta)

jogo_forca()