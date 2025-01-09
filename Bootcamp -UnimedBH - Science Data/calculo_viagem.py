# Calcular e mostra litros_gastos, sendo que a cada 12Km faz 1L.
# tempo em h; veloc em km/h.
# print(f'{litros_gastos:.3f}')
def calculador_litros(veloc, tempo):

    km_litro = 12
    delta_s = veloc * tempo

    litros_necessarios = delta_s / km_litro

    return litros_necessarios

scan = input().split()
veloc = int(scan[1])
tempo = int(scan[0])

litros_gastos = calculador_litros(veloc, tempo)
print(f'{litros_gastos:.3f}')





    
