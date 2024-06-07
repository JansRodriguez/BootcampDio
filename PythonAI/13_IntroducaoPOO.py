""" 
    Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente. 
    Já os objetos, podemos utiliza-los, pois eles possuem as características e comportamentos que foram defindidos nas classes.
    CLASSES =  são algo abstratos
    OBJETOS =  são itens mais concretos, utilizáveis.

    Exemplo:
    A planta de uma casa é o algo abstrato da casa, o modelo.
    A casa em si, é o objeto, o item real, do projeto PLANTA
"""
    ### DEFININDO UMA CLASSE
"""class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.name = nome
        self.color = cor
        self.awaked = acordado
    
    def latir(self):
        print("auau")

    def dormir(self):
        self.awaked = False
        print('Zzzzz...')

caoUm = Cachorro('Bento', 'pardo')
carDois = Cachorro('Piti', 'verde pardo')

print(carDois.awaked)

"Crie um programa que informe: cor, modelo, ano e valor da bicicleta vendida. Uma bicicleta pode: buzinar, parar e correr; Adicione esses comportamentos"

class vendaBicicleta:
        ## ATRIBUTOS DA CLASSE
    def __init__(self, cor, modelo, ano, valor):
        self.color = cor
        self.model = modelo
        self.year = ano
        self.value = valor

        ## COMPORTAMENTOS DA CLASSE
    def buzinar(self):
        print('Plim Plim')

    def parar(self):
        print('iiiiiiir')
    
    def correr(self):
        print('vRUM... vRUM')
## Quando utilizamos o argumento self, estamos passando o próprio objeto
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

bicicletaUm = vendaBicicleta('verde', 'atletica', 2019, 1090.89)

bicicletaUm.buzinar() # ou -> vendaBicicleta.buzinar(bicicletaUm)
bicicletaUm.parar()
bicicletaUm.correr()
bicicletaUm.__str__

print(bicicletaUm.model)
print(f'O valor da bicicleta é: {bicicletaUm.value}')
print(bicicletaUm.year)
print(bicicletaUm.color)
print(bicicletaUm)
"""
    ## MÉTODOS CONSTRUTORES E DESTRUTORES
        ## MÉTODO CONSTRUTOR
""" 
    O método construtor sempre é executado quando uma nova instância da classe é criada.
    Nesse método, inicializamos o estado do nosso objeto.    
    Para declarar o método construtor da classe, criamos um método com o nome __init__

        ## MÉTODO DESTRUTOR
    Para declarar o método destrutor da classe, criamos um me´todo com o nome __del__

class Gato:
    def __init__(self, nome, cor, acordado = True) -> None:
        print('Estou inicializando a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        print('Classe inicializada.')

##cachorroUm = Gato('Breen', 'amarelo')
# Uma função/método pode ser criado utilizando a clase ja existente.
def criarCachorro():
    c = Gato('Zeus', 'Preto', False)
    print(c.nome)
criarCachorro()
"""
