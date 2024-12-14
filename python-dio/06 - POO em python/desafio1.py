# TODO: Crie uma classe e método para realizar a soma:
class Calculadora:

    def soma(self, num1, num2):
        #o metodo precisa  do self para dizer que a classe acessa ele e os resultados
        resultado = num1 + num2

        return resultado



num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)