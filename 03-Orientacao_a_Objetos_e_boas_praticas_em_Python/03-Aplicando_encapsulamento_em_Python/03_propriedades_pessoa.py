class Pessoa:
    def __init__(self, nome, ano_nascimento) -> None:
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Ester", 1998)
print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}")