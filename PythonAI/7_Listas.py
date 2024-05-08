""" 
    Listas em python podem armazenar de maneira sequencial qualquer tipo de objeto.
    Podemos criar listas utilizando o construtor LIST, a função RANGE, ou colocando os valores em colchetes, separados por vírgulas.
    Listas são objetos mutáveis, podendo sofrer alterações após sua criação
    #Lista de uma STRING
curso = 'python'
print(curso)
print(list(curso))
# O construtor LIST solicita um elemento iteravel, por isso sua resposta será uma lista com cada letra do curso, um elemento de lista.
    #Lista da função RANGE
numeros = list(range(10))
print(f'O valor do último index numeros[9] = {numeros[9]}, é o mesmo valor do index numeros[-1] =  {numeros[-1]}')
    ## Trabalhando com MATRIZ
matriz = [
    [1, "-a", 11],
    ["b", 7, "z"],
    [3, 7, 8]
]
print(f'Trazendo a matriz {matriz}')
print(f'Trazendo o primeiro indice da matriz, matriz[0]: {matriz[0]}')
print(f'Trazendo o segundo indice da matriz e o junto elemento, matriz[1][-2]: {matriz[1][-2]}')
print(f'Trazendo o ultima indice da matriz e o ultimo elemento, matriz[-1][-1]: {matriz[-1][-1]}')
print(f'Trazendo a primeira linda e a ultima linhda da matriz, matriz[0:3:2]: {matriz[0:3:2]}')
    ## para ITERAR LISTAS, a forma mais comum é utilizar o comando FOR
carros = ["gol", "fiat", "volks"]

for carro in carros:
    if carro == carros[0]:
        print("="*len(max(carros)))
    print(carro)
    print("="*len(carro))
        ## Função ENUMERATE dentro do FOR
carros = ["gol", "fiat", "volks"]
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')
        ## COMPREENSÃO DE LISTAS
#A COMPREENSÃO DE LISTAS oferece uma sintae mais curta quando você deseja criar uma nova lista com base nos valores de uma lista existente(filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.
    ## Versão comum
numeros = [1, 10, 12, 14, 21, 52, 5]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(f'Pares com for: {pares}')
    ## COMPREENSÃO
numeros = [1, 10, 12, 14, 21, 52, 5]
pares = [numero for numero in numeros if numero % 2 == 0] ## COMO SE LER: retorne NUMERO, para cada numero em números, se o resto da divisão de numero por 2 for igual a ZERO (0)
print(f'Pares com COMPREENSÃO DE LISTAS: {pares}')
numeros = [1, 10, 12, 14, 21, 52, 5]
quadradro = [numero ** 2 for numero in numeros]
print(f'Quadrado com COMPREENSÃO DE LISTAS: {quadradro}')
"""
## MÉTODS PARA CLASSE LISTA
    # APPEND (ADICIONAR ELEMENTOS A LISTA)
    # CLEAR (LIMPAR A LISTA)
    # COPY (COPIA LISTA OU ELEMENTOS)
    # COUNT (CONTA A OCORRÊNCIA DE DETERMINADO ELEMENTO DA LISTA)
    # EXTEND (ADICIONA ELEMENTO EM UMA LISTA PRIMÁRIA, PODENDO SER OUTRA LISTA, SEM REMOVER DUPLICATA)
    # INDEX (RETORNA A POSIÇÃO EM INDEX DE DETERMINADO ELEMENTO DA LISTA, SE HOUVER VALOR DUPLICADO, ELE RETORNA A PRIMEIRA OCORRÊNCIA)
    # POP (REMOVE O ULTIMO ELEMENTO DA LISTA[-1], NO ENTANTO, PODEMOS ESPECIFICAR QUAL ELEMENTO DESEJAMOS REMOVER, UTILIZANDO O INDICE)
    # REMOVE (REMOVE ELEMENTOS DE LISTA, ESPECIFICANDO O ELEMENTO, REMOVENDO A PRIMEIRA OCORENCIA DO ELEMENTO)
    # REVERSE (RETORNA A LISTA AO CONTRÁRIO)
    # SORT (ORDENA A LISTA POR ORDEM NUMÉRICA, ALFABÉTICA, TAMANHO, ALFABÉTICA AO CONTRÁRIO, SE UTILIZANDO DOS ARGUMENTOS REVERSE E KEY)
    # LEN (RETORNA O TAMANHO DA LISTA)
    # SORTED (RETORNA OS ELEMENTOS DA LISTA EM ORDEM)