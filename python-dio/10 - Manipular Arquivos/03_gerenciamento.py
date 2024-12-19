import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# print(ROOT_PATH.parent) --> tudo ate a pasta \10 - Manipular Arquivos

# os.mkdir(ROOT_PATH / "novo-diretorio")

file = open(ROOT_PATH / "novo.txt", "w")
file.close()

# os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")

# file = open("")