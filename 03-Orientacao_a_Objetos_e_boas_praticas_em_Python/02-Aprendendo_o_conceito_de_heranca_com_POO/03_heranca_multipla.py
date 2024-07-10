class Animal:
    def __init__(self, nr_patas):
        self.nr_patas = nr_patas
        
    def __str__(self):
        return f"{__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(nr_patas = 4, cor_pelo = "Preta")
print(gato)

ornitorrinco = Ornitorrinco(nr_patas = 4, cor_pelo = "Marrom", cor_bico = "Amarela" )
print(ornitorrinco)