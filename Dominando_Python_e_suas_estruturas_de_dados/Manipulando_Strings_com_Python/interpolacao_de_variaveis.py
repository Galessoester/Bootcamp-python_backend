nome = "Ester"
idade = 26
profissao = "Programadora"
linguagem = "Python"

# Forma antiga, não deve mais funcionar no python 3
# print("Olá. me chamo %s. Tenho %d anos de idade. Trabalho como %s e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))

# format
print("Olá, me chamo {}. Tenho {} anos de idade. Trabalho como {} e estou matriculada no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {2}. Tenho {1} anos de idade. Trabalho como {3} e estou matriculada no curso de {0}.".format(linguagem, idade, nome, profissao))

print("Olá, me chamo {nome}. Tenho {idade} anos de idade. Trabalho como {profissao} e estou matriculada no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# f-string
print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade. Trabalho como {profissao} e estou matriculada no curso de {linguagem}.")

pi = 3.14159

# Formata o número para conter apenas duas casas após a virgula
print(f"Valor de pi: {pi:.2f}")

# Adiciona espaços a esquerda
print(f"Valor de pi: {pi:10.2f}")