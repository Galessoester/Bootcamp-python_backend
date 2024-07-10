class Veiculo:
    def __init__(self, cor, marca, placa, nr_rodas):
        self.cor = cor
        self.marca = marca
        self.placa = placa
        self.nr_rodas = nr_rodas
    
    def ligar_motor(self):
        print("Ligando o motor ...")
        
    def __str__(self):
        return f"{__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
       

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, marca, placa, nr_rodas, carregado):
        super().__init__(cor, marca, placa, nr_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} está carregado")


moto = Motocicleta("Vermelha", "Yamaha", "abc-1234", 2)
print(moto)
moto.ligar_motor()

carro = Carro("Preto", "Fiat", "yuo-4567", 5)
carro.ligar_motor()

caminhao = Caminhao("Vermelho", "Scania", "cbn-2145", 8, True)
caminhao.esta_carregado()
