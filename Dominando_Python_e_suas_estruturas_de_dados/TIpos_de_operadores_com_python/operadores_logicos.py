# AND
print(True and True)
print(True and False)
print(False and False)

# OR
print(True or True)
print(False or False)

saldo = 5000
saque = 250
limite = 200
especial = False

exp = saque >= saldo and saque <= limite or especial and saldo >= saque
print(exp)

exp_2 = (saque >= saldo and saque <= limite) or (especial and saldo >= saque)
print(exp_2)

