import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

# try:
    # with open(ROOT_PATH / "arquivo_csv.csv", "w", newline='', encoding="utf-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(['id', 'nome'])
#         escritor.writerow([1, 'Maria'])
#         escritor.writerow([2, 'João'])
# except IOError as exc:
#     print("Erro ao criar arquivo. {exc}")



# try:
#     with open(ROOT_PATH / "arquivo_csv.csv", "r", newline='', encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for row in leitor:
#             print(row)
# except IOError as exc:
#     print("Erro ao ler arquivo. {exc}")



# try:
#     with open(ROOT_PATH / "arquivo_csv.csv", "r", newline='', encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for idx, row in enumerate(leitor):
#             if idx == 0:
#                 continue
#             print(f"ID: {row[COLUNA_ID]}")
#             print(f"Nome: {row[COLUNA_NOME]}")
# except IOError as exc:
#     print("Erro ao ler arquivo. {exc}")



try:
    with open(ROOT_PATH / "arquivo_csv.csv", "r", newline='', encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print("Erro ao ler arquivo. {exc}")