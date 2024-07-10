class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print("Instanciando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def latir(self):
        print("Auau!")

    def __del__(self):
        print("Deletando a instância da classe...")
        

bob = Cachorro("Bob", "Caramelo")
belinha = Cachorro("Belinha", "preta")

bob.latir()

del belinha

def criar_cachorro():
    hercules = Cachorro("Hércules", "Branco")
    print(hercules.nome)
    
criar_cachorro()