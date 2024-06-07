""" 
    É a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base)

    ###  EXEMPLO:
class A:
    pass
class B(A):
    pass
    ## HERANÇA SIMPLES X HERANÇA MÚLTIPLA
## O Exemplo acima é o conceito de herança simples.
class C:
    pass
class D:
    pass
class E(C, D):
    pass
    
        ## Herança Simples

class Veiculo:
    def __init__(self, placa, nroRodas, nroChassi):
        self.placa = placa
        self.nro_rodas = nroRodas
        self.nro_chassi = nroChassi

    def ligarMotor(self):
        print("Ligando veículo")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhão(Veiculo):
    def __init__(self, placa, nroRodas, nroChassi, carregado):
        self.carregado = carregado
        super().__init__(placa, nroRodas, nroChassi)
        
    def estaCarregado(self):
        print(f'{'Sim' if self.carregado else 'Não'}, estou carregado')

moto1 = Motocicleta('q234', 2, 9876)

carro1 = Carro('583d', 4, '9wh3502j')

caminhao1 = Caminhão('892n', 12, 'cnd0284n', False)
caminhao1.estaCarregado()
print(moto1)
print(carro1)
print(caminhao1)
"""

        ## Herança Múltiplas