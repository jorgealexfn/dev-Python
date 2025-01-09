
def n_med_consumidos(P,H):
    M = P / H
    return M

while True:
    try:
        scan = input().split() 
        P = int(scan[0])
        H = int(scan[1])
        if 1 <= P <= 1000 and 1 <= H <= 1000 :
            resultado_consumido = n_med_consumidos(P, H)
            print(f'{resultado_consumido:.2f}')
        else:
                raise ValueError("Valor invalido. Deve ser entre 1 e 1000.")
    except ValueError as e:
            print(e)
            




