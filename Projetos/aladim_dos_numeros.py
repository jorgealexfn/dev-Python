import random

numero_secreto = random.randint(1, 100)
tentativas = 0
tentativas_maximas = 7

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

while True:
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
