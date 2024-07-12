from pathlib import Path

ROOT_PATH = Path(__file__).parent

# With fecha o arquivo mesmo com erro no código
# with open(ROOT_PATH / "arquivo.txt", "r") as arquivo:
#     print("trabalhando com o arquivo")
# print(arquivo.read())

# with open(ROOT_PATH / "arquivo.txt", "r") as arquivo:
#     1 / 0
# print(arquivo.read())


# try:
#     with open(ROOT_PATH / "arquivo1.txt", "r") as arquivo:
#         print("trabalhando com o arquivo")
#     print(arquivo.read())
# except IOError:
#     print("Não foi possivel abrir o arquivo.")

# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Esse caracter não existe em ascii: ÿ")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo. {exc}")


try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo. {exc}")
except UnicodeDecodeError as exc:
    print(f"Erro ao ler o arquivo. {exc}")