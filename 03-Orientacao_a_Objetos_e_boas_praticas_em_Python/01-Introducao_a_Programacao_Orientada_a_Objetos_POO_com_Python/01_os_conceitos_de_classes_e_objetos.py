class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def latir(self):
        print("Auau!")
    
    def dormir(self):
        self.acordado = False
        print("Zzzz...")
        
bob = Cachorro("Bob", "Caramelo")
belinha = Cachorro("Belinha", "preta")

bob.latir()

print(belinha.acordado)
belinha.dormir()
print(belinha.acordado)