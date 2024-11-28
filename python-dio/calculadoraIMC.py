
def calcular_imc(altura, peso):
    
    imc = peso / (altura * altura)
    

    return imc

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso:"))

# Chama a função para calcular o IMC
resultado_imc = calcular_imc(altura, peso)
    
if resultado_imc < 18.5:
    print("Abaixo do peso, atenção! procure um médico ")
elif 18.5 <= resultado_imc < 25 :
    print("peso normal, Excelente")
elif 25 <= resultado_imc < 30 :
    print("Sobrepeso..., faça exercícios!")
else:
    print("Obesidade, PROCURE UM MÉDICO URGENTE! ")

