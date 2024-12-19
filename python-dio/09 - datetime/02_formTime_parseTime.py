# import datetime

# d = datetime.datetime.now()

# print(d.strftime("%d/%m/%Y %H:%M"))

# data_string = "20/07/2023 15:30"
# d = datetime.datetime.strptime(data_string, "%d/%m/%Y %H:%M")
# print(d)

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20  20:23"
mascara_ptBr= "%d/%m/%Y %a"
mascara_en= "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptBr))

dataConvertida = datetime.strptime(data_hora_str, mascara_en)