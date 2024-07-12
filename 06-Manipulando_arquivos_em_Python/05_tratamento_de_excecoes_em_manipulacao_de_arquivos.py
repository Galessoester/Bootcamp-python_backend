from pathlib import Path

ROOT_PATH = Path(__file__).parent


try:
    # arquivo = open("meu_arquivo.txt") # [Errno 2] No such file or directory: 'meu_arquivo.txt'
    # arquivo = open(ROOT_PATH / "novo-diretorio") # Erro ao abrir o arquivo: [Errno 13] 
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r") # Funciona normalmente
    arquivo.close()
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")