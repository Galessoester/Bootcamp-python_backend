saldo = 1000
limite = 500

print(saldo is limite) # False, porque eles estão ocupando espaços diferentes de memória, mas a expressão diz que eles estão

print(saldo is not limite) # True, porque aqui ela verifica se eles não estão na mesma parte da memória, o que é verdade, então True.