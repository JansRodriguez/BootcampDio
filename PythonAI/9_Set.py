    #CONJUNTOS
""" 
    É uma coleção que não possui objetos  repetidos. Usamos SET para representar um conjunto matemático ou eliminar  itens duplicados de um iterável.
    A representação de um conjunto é que CHAVES { }
    Conjuntos em Python não suportam indexação e nem fatiamento e com isso, modificação. Para acessar, é necessário converter para lista.

lista = [1, 2, 1, 4, 3, 5, 3]
conjunto = set(lista)
conjunto2 = set('Abacaxi')
carros = set(("gol", "fiat", "volks", "volks", "volks"))

print(lista)
print(conjunto)
print(conjunto2)
print(carros)

print(type(conjunto))
print(type(conjunto2))
print(type(carros))

linguagens = {"java", "c", "java", "python"}
print(linguagens)
print(type(linguagens))
    ## para ITERAR CONJUNTOS, a forma mais comum é utilizar o comando FOR. Lembrando que primeiro é necessário transformar os SET em LIST
carros = {"gol", "fiat", "volks"}
print(type(carros))
print('Convertendo CONJUNTO em lista')
carros = list(carros)

for carro in carros:
    if carro == carros[0]:
        print("="*len(max(carros)))
    print(carro)
    print("="*len(carro))
"""
## Função ENUMERATE dentro do FOR
carros = {"gol", "fiat", "volks"}
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

## MÉTODS PARA CLASSE SET
    # UNION (UNI CONJUNTOS) setA.union(setB)
    # INTERSECTION (REALIZA A INTERSECÇÃO DE CONJUNTOS) setA.intersection(setB)
    # DIFFERENCE (VERIFICA QUAIS ELEMENTOS DO PRIMEIRO CONJUNTO QUE NÃO ESTÃO NO SEGUNDO CONJUNTO) Le-se: O que temos em A que não temos em B
    # SYMMETRIC_DIFFERENCE (MAPEIA QUAIS ELEMENTOS NÃO SÃO COMUNS EM DOIS CONJUNTOS)
    # ISSUBSET (VERIFICA SE UM CONJUNTO É SUBCONJUNTO DE OUTRO CONJUNTO)
    # ISSUPERSET (VERIFICA SE TODOS OS ELEMENTOS DE UM CONJUNTO ESTÃO PRESENTES EM OUTRO CONJUNTO)
    # ISDISJOINT (VERIFICA SE OS ELEMENTOS DO 1º CONJUNTO NÃO PERTENCEM AO 2º CONJUNTO)
    # ADD (ADICIONA ELEMENTOS EM UM CONJUNTO, MANTENDO A REGRA DA NÃO DUPLICATA)
    # CLEAR (REMOVE TODOS OS ELEMENTOS DO CONJUNTO)
    # COPY (COPIA OS ELEMENTOS DO PRIMEIRO CONJUNTO)
    # DISCARD (NECESSITA DE ARGUMENTO NO MÉTODO, REMOVE O ELEMENTO REFERIDO)
    # POP (REMOVE OS ELEMENTOS EM ORDENAÇÃO )
    # REMOVE (REMOVE OS ELEMENTOS INDICADOS NO ARGUMENTO)
    # LEN (O TAMANHO DO CONJUNTO, QUANTIDADE DE ELEMENTOS)
    # IN (VERIFICA SE O ELEMENTO ESTAR CONTIDO NO CONJUNTO)