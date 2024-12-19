# import datetime

# data = datetime.datetime(2023, 7, 19, 13, 45)
# print(data)

# data = data + datetime.timedelta(weeks=1)
# print(data)
from datetime import timedelta, datetime, timezone

tipo_carro = "M"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.now()

if tipo_carro=="P":
    estimativa = data_atual + timedelta(minutes=tempo_pequeno)
    print(f" O carro chegou: {data_atual} e ficará pronto às {estimativa}")
elif tipo_carro=="M":
    estimativa = data_atual + timedelta(minutes=tempo_medio)
    print(f" O carro chegou: {data_atual} e ficará pronto às {estimativa}")
else:
    estimativa = data_atual + timedelta(minutes=tempo_grande)
    print(f" O carro chegou: {data_atual} e ficará pronto às {estimativa}")