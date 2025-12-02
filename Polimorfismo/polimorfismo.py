class Passaro:
    def voar(self):
        print("Voando")
    
class pardal(Passaro):
    def voar(self):
        super().voar()
    
class avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")
    
def plano_voo(obj):
    obj.voar()

p1 = pardal()
p2 = avestruz()


plano_voo(p1)
plano_voo(p2)