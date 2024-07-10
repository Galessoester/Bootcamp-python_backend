class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Prim prim!")
    
    def parar(self):
        print("Parando a bicicleta")
        print("Bicicleta parada")
        
    def correr(self):
        print("Vruuuuuuum....")
        
    # Define uma forma bonita e dinâmica de mostrar os dados do objeto
    def __str__(self):
        return f"{__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
bici_1 = Bicicleta("Vermelha", "Caloi", 2022, 600)

bici_1.correr()
bici_1.buzinar()
bici_1.parar()
print(bici_1.cor, bici_1.modelo, bici_1.ano, bici_1.valor)

bici_2 = Bicicleta("Verde", "Monark", 2000, 190)
Bicicleta.buzinar(bici_2)
print(bici_2)