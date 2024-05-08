"""
    Função é um bloco de código identificado por um nome e pode receber uma lista de parametros, esses parametros podem ou não ter valores padrões.
    Usar funções, torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada.
   
    # Função sem retorno:
def exibir_mensagem():
    print("Olá, mundo!")
exibir_mensagem()

def exibir_mensagem2(nome):
    print(f'Olá, mundo e {nome}')
exibir_mensagem2("Victor")

def exibir_mensagem3(nome="alunos"):
    print(f"Olá, mundo e {nome}")
exibir_mensagem3()

def exibir_mensagem4(nome, cor):
    print(f'Olá, mundo e {cor} {nome}')
exibir_mensagem4("Janes", "amarelo")
    # Função com retorno: - em Python uma função pode retornar mais de um valor
def somarNumeros(listaNumeros):
    return sum(listaNumeros)
print(somarNumeros([2, 2, 2, 1]))

def antecessorSucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor
print(antecessorSucessor(10))
    # Argumentos nomeados: funções também podem ser chamadas utilizando argumentos nomeados da forma chave:valor
def salvarCarro (marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')
salvarCarro('Fiat', 'Palio', 1999, 'ABC-1234')
salvarCarro(marca='Volks', modelo='Gol', ano=2013, placa='SAD-3253')
salvarCarro(**{"marca":"Fiat", "modelo": "Palio", "ano": 2018, "placa":"GHT-9857"})
    # OBJETO DE PRIMEIRA CLASSE - Podemos atribuir funções a variaveis, passá-las como parametro para funções, usá-las como  estruturas de dados (listas, tuplas, dicionários) e usar como valor de retorno para a função (clousures)
def somar(a, b):
    return a + b
def exibirResultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado  da operação {a} + {b} = {resultado}')
exibirResultado(10, 20, somar)
        # variavel recebendo a função
variavel = somar
print(variavel(2, 12))
""" 
    # ESCOPO GLOBAL E ESCOPO LOCAL
