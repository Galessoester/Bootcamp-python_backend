curso = "pYthON"

# Todas as letras maiúsculas
print(curso.upper())

# Todas as letras minúsculas
print(curso.lower())

# A primeira letra maiúscula
print(curso.title())

curso = "    Python  "

# remover todos os espaços 
print(curso.strip())

# Remover os espaços da esquerda
print(curso.lstrip())

# Remover os espaços da direita
print(curso.rstrip())

curso = "Python"

# Centralizar a string no meio dos caracteres (o segundo parâmetro "#" é opcional, será substituido por espaços em branco)
print(curso.center(10, "#"))

# Colocar caracteres no meio da string
print(".".join(curso))