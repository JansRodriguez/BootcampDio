""" 
    As tuplas são conjuntos de elementos imutáveis, muito parecido com as listas. Sendo sua criação através da classe TUPLE, ou colocando valores separados por vírgulas dentro dos parenteses.
    Para a criação de TUPLAS, utilizamos o construtor TUPLE, valores separados por vírgulas, e converter listas em tuplas.
    Quando se tem uma tupla de apenas um valor, é necessário colocar uma virgula no final, para o interpretador identificar que aquele valor é uma tupla, não uma string.

frutas = ("laranja", 'banana', 'uva')
fruta = ("banana",)
letras = tuple("Python")
numeros = [1, 2, 3, 4, 5]
numeros = tuple(numeros)

print(frutas)
print(fruta)
print(letras)
print(numeros)

print(type(frutas))
print(type(fruta))
print(type(letras))
print(type(numeros))

matriz = (
    (1, "-a", 11),
    ("b", 7, "z"),
    (3, 7, 8)
)
print(f'Trazendo a matriz {matriz}')
print(f'Trazendo o primeiro indice da matriz, matriz[0]: {matriz[0]}')
print(f'Trazendo o segundo indice da matriz e o junto elemento, matriz[1][-2]: {matriz[1][-2]}')
print(f'Trazendo o ultima indice da matriz e o ultimo elemento, matriz[-1][-1]: {matriz[-1][-1]}')
print(f'Trazendo a primeira linda e a ultima linhda da matriz, matriz[0:3:2]: {matriz[0:3:2]}')
    ## para ITERAR TUPLAS, a forma mais comum é utilizar o comando FOR
carros = ("gol", "fiat", "volks")

for carro in carros:
    if carro == carros[0]:
        print("="*len(max(carros)))
    print(carro)
    print("="*len(carro))
print(type(carros))

        ## Função ENUMERATE dentro do FOR
carros = ("gol", "fiat", "volks")
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')
print(type(carros))
"""
        ## MÉTODS PARA CLASSE LISTA
    # COUNT (CONTA A OCORRÊNCIA DE DETERMINADO ELEMENTO DA TUPLA)
    # LEN (RETORNA O TAMANHO DA TUPLA)
    # INDEX (RETORNA A POSIÇÃO EM INDEX DE DETERMINADO ELEMENTO DA TUPLA, SE HOUVER VALOR DUPLICADO, ELE RETORNA A PRIMEIRA OCORRÊNCIA)
carros = ("gol")
print(isinstance(carros, tuple))