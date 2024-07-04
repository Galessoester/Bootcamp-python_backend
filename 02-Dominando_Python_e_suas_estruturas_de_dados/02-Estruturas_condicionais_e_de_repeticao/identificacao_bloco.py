
saldo = 500
def sacar(valor): # Início do método sacar

    if saldo >= valor: # Início do bloco if
        print('Valor sacado') # Só será executado se a verificação for verdadeira
        print('Retire o dinheiro na boca do caixa.') # Só será executado se a verificação for verdadeira
    # Fim do bloco if

    print('Obrigada por ser nosso cliente!') # Será executado em todas as ocasiões por estar dentro do método sacar

# Fim do método sacar

print(sacar(100))

def depositar(valor):
    saldo = 500
    saldo += valor
    print(saldo)

depositar(10)