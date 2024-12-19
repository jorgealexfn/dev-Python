import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

# try:
#     with open(ROOT_PATH / "usuarios.csv", "w", encoding="utf-8") as file:
#         escritor = csv.writer(file)
#         escritor.writerow(["id", "Nome"])
#         escritor.writerow(["1", "Jorge"])
#         escritor.writerow(["2", "Thamyres"])
# except IOError as exc:
#     print("Erro ao criar o arquivo. {exc}")

try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as file:
        leitor = csv.reader(file)
        for row in leitor:
            print(row[COLUNA_ID], row[COLUNA_NOME])

except IOError as exc:
    print("Erro ao criar o arquivo. {exc}")