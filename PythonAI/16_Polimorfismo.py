""" 
    O POLIMORFISMO significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes.
"""
class Passaro:
    def voar(self):
        print('...voando!!!')
class Pardal(Passaro):
    def voar(self):
        return super().voar()
        print('Pardal voa!!!')
class Galinha(Passaro):
    def voar(self):
        ##return super().voar()
        print('Galinha não voa!!!')

def planoVoo(obj):
    obj.voar()

planoVoo(Pardal())
planoVoo(Galinha())