
def calculador_ICM(n,x,y):

    icm_calculado = n / (x + y)

    return icm_calculado


entrada = input().split()

n = int(entrada[0])
x = int(entrada[1])
y = int(entrada[2])

resultado_comunicacao = calculador_ICM(n,x,y)

print(f'{resultado_comunicacao:.2f}')