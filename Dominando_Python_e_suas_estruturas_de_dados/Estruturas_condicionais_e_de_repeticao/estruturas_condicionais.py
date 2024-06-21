verdade = True
mentira = False

if mentira:
    print('É mentira!') # Esta linha de código nunca vai rodar porque mentira é false e não vai ser validada pelo if

if verdade:
    print('É verdade!')
else:
    print('É mentira!')

if not mentira:
    print('Não é mentira!')
else:
    print('É mentira!') # Esta linha de código nunca vai rodar porque mentira é false e não vai ser validada pelo if


escolha = int(input('Escolha uma opção:\n1. Sacar\n2. Depositar\n0. Finalizar operação\n'))

saldo = 500.0


while escolha != 0:
    if escolha == 1:
        saque = float(input('Informe o valor desejado: '))
        if saldo >= saque:
            saldo -= saque
            print('Saque realizado com sucesso! Saldo atual: ' + str(saldo))
        else:
            print('Saldo insuficiente!')
        escolha = int(input('Escolha uma opção:\n1. Sacar\n2. Depositar\n0. Finalizar operação\n'))
    elif escolha == 2:
        deposito = float(input('Informe o valor desejado: '))
        saldo += deposito
        print('Depósito realizado com sucesso! Saldo atual: ' + str(saldo))
        escolha = int(input('Escolha uma opção:\n1. Sacar\n2. Depositar\n0. Finalizar operação\n'))
    else:
        print('Opção inválida!')
        escolha = int(input('Escolha uma opção: \n1. Sacar\n2. Depositar\n0. Finalizar operação\n'))
