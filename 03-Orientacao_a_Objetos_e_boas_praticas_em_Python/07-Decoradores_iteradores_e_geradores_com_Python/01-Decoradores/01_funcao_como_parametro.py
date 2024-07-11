def mensagem(nome):
    print("Executando a função mensagem")
    return f"Oi {nome}"


def mensagem_longa(nome):
    print("Executando a função mensagem_longa")
    return f"Oi {nome}, tudo bem com você?"

def executar(funcao, nome):
    print("Executando a função executar")
    return funcao(nome)

print(executar(mensagem, "Ester"))
print(executar(mensagem_longa, "Ester"))