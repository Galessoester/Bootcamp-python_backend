class Passaro:
    def voar(self):
        print("Voando...")
        
class Pardal(Passaro):
    pass

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa.")
        
def plano_de_voo(obj):
    obj.voar()
    
plano_de_voo(Pardal())
plano_de_voo(Avestruz())