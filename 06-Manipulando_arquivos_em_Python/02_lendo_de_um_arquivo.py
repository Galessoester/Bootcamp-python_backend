file = open('C:/Users/Esther/OneDrive/Projetos/Bootcamp-python_backend/06-Manipulando_arquivos_em_Python/arquivo.txt', "r")

print(file.read())
print(file.readline())
print(file.readlines())

file.close()
