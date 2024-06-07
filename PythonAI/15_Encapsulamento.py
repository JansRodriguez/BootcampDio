""" 
    Ele descreve a ideia de agrupar dados e os métodos que manipulam esses dados em uma unidade.
    Isso impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados.
    Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto.
    Agrupamento semântico: Dentro da classe, ela gerencia os dados que estão dentro dela.

    - MODIFICADORES DE ACESSO:
    Em Python, não temos palavas reservadas, porém usamos convenções no nome do recurso, para definir se a variável é pública ou privada.

    Para acessar uma variável privada em python, necessitamos criar um método para tal ação.

class Conta:
    def __init__(self, nroAgencia, saldo=0) -> None:
        self._saldo = saldo
        self.nroAgencia = nroAgencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo

conta1 = Conta('00n1', 100)

print(conta1.mostrar_saldo())
conta1.depositar(150)
print(conta1.mostrar_saldo())
conta1.sacar(50)
print(conta1.mostrar_saldo())


    ## USO DO PROPERTY no encapsulamento
class FOO:
    def __init__(self, x = None):
        self._x = x

    @property ## Atributo gerenciado.
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, valor):
        ##self._x += valor
        self._x = valor
    
foo = FOO(10)
print(foo.x) # Inves de chamar o método, estou chamando a característica da classe.
foo.x = 11
print(foo.x)
"""
    ## Exemplo 2 - PROPERTY
class Pessoa:
    def __init__(self, nome, nascimento) -> None:
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _anoAtual = 2024
        return _anoAtual - self._nascimento
pessoa = Pessoa('Janes', 1988)

print(f'Nome: {pessoa.nome}\nIdade: {pessoa.idade}')