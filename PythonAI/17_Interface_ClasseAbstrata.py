""" 
    Todos os objetos nascem com o mesmo número de atibutos de classe e instância. 
    Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

class Estudante:

    escola  = 'DIO'

    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = matricula
    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula}  - {self.escola}'

def mostraValores(*objs):
    for obj in objs:
        print(obj)

    
aluno1 = Estudante('Vitoria', 143)
aluno2 = Estudante('Gabriel', 9834)

mostraValores(aluno1, aluno2)

print("*="*5)

aluno2.escola = 'ADA'

mostraValores(aluno1, aluno2)

Estudante.escola = 'ADA'

mostraValores(aluno1, aluno2)
"""
    ## MÉTODO DE CLASSE E MÉTODOS ESTÁTICOS
        ## MÉTODO DE CLASSE
            ## Métodos de classe estão ligados à classe e não ao objeto. 
            # Eles têm acesso ao estado da classe, pois recebem um parametro que aponta para a classe e não para a instância do objeto
        ## MÉTODOS ESTÁTICOS
            ## Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe. 
        ## DIFERENÇAS
            ## Um método de classe recebe um primeiro parametro que aponta para a classe, enquanto um método estático não.
            ## Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.
        ## QUANDO UTILIZAR
            ## Geralmente usamos o método de classe para criar métodos de fábrica (método que retorna instância da classe).
            ## Geralmente usamos métodos estáticos para criar funções utilitárias (funções de validação).

    ## INTERFACE e CLASSES ABSTRATAS

