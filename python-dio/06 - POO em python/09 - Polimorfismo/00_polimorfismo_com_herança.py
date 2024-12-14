class Passaro:
    def voar(self):
        print("Voando... BRUF BRUF BRUF")

class Pardal(Passaro):
    def voar(Self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz nao voa, de menor")

def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()


plano_de_voo(p1)
plano_de_voo(p2)