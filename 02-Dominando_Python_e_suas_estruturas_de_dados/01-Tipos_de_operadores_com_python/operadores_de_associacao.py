frutas = ['limão', 'Uva']
curso = 'Curso de Python'

print('maçã' in frutas) # False, porque não existe a palavra 'maçã' na sequência de frutas

print('uva' in frutas) # False, porque a função é case sensitive, ou seja estamos verificando se 'uva' (com letra minuscula) é igual a 'Uva' (com letra maiuscula)

print('limão' in frutas) # True, porque existe a palavra 'limão' em frutas, exatamente como está escrito

print('limao' not in frutas) # True, porque limão está escrito sem o acento 'til' e estamos verificando se a palavra NÃO ESTÁ na variável frutas

print('p' in curso) # False, porque a letra 'p' está maiuscula em curso e estamos verificando um 'p' minúsculo

print('python' not in curso) # False, pelo mesmo motivo do exemplo acima


