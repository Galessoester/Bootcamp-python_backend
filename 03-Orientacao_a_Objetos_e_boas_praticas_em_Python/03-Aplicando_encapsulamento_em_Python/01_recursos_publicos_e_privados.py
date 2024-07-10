class Conta:
    def __init__(self, nr_agencia, saldo = 0):
        self._saldo = saldo
        self.nr_agencia = nr_agencia
    
    def depositar(self, valor):
        self._saldo += valor
        
    def sacar(self, valor):
        self._saldo -= valor
        
    def mostrar_saldo(self):
        return self._saldo
        
conta = Conta(1, 1000)
conta.depositar(200)
conta.sacar(50)
print(conta.nr_agencia)
print(conta.mostrar_saldo())