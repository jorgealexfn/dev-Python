import tkinter as tk
import random

def verificar_palpite():
    palpite_usuario = int(entrada_palpite.get())
    global tentativas
    tentativas += 1

    if palpite_usuario == numero_secreto:
        resultado_label.config(text=f"Parabéns! Você acertou em {tentativas} tentativas.")
        botao_verificar.config(state=tk.DISABLED)
    elif palpite_usuario < numero_secreto:
        resultado_label.config(text="O número secreto é maior.")
    else:
        resultado_label.config(text="O número secreto é menor.")

# ... resto do código

# Inicializando o jogo
numero_secreto = random.randint(1, 100)
tentativas = 0

# Criando a janela
janela = tk.Tk()
janela.title("Adivinhe o número")

# Criando os elementos da interface
rotulo_instrucoes = tk.Label(janela, text="Adivinhe o número entre 1 e 100")
rotulo_instrucoes.pack()

entrada_palpite = tk.Entry(janela)
entrada_palpite.pack()

botao_verificar = tk.Button(janela, text="Verificar", command=verificar_palpite)
botao_verificar.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Iniciando o loop principal
janela.mainloop()