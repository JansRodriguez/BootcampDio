""" 
    Dicionário é um conjunto não-ordenado de pares 'chave:valor', onde as chaves são únicas em uma dada instância do dicionário.
    Dicionários são delimitados por chaves: { }, e contém uma lista de pares 'chave:valor' separados por vírgulas.
    Os elementos do dicionário são acessados e modificados através das chave
pessoa = {
    "nome" : "Guilherme",
    "idade": 32
}
pessoa = dict(apelido="Vinicius", tempoVida = 19)
pessoa['nick'] = 'Gabriel'

print(pessoa)
print(type(pessoa))

    ## Acessando valores do DICIONÁRIO - O retorno será o valor, acessa-se com a chave
pessoa = {
    "nome" : "Guilherme",
    "idade": 32,
    "cidade": "São Luís"
}
print(pessoa)
print(pessoa["cidade"])
        # Subescrevendo os valores das chaves
pessoa["cidade"] = "Brasilia"
pessoa["idade"] = 27
pessoa["nome"] = "Tome"

print(pessoa)
    ## DICIONÁRIOS ANINHADOS
contatos = {
    "nome1@gmail.com" : {
        "nome": "NomeUm",
        "telefone": 123456
    },
    "nome2@gmail.com" : {
        "nome": "NomeDois",
        "telefone": 654321
    }
}

print(contatos)
print(type(contatos))
print(contatos["nome1@gmail.com"])
print(contatos["nome1@gmail.com"]["telefone"])
    ## para ITERAR DICIONÁRIOS, a forma mais comum é utilizar o comando FOR
contatos = {
    "nome1@gmail.com" : {
        "nome": "NomeUm",
        "telefone": 123456
    },
    "nome2@gmail.com" : {
        "nome": "NomeDois",
        "telefone": 654321
    }
}
for chave in contatos:
    print(chave, contatos[chave])
for chave, valor in contatos.items():
    print(chave, valor)
"""
## MÉTODS PARA CLASSE LISTA
    # CLEAR (LIMPAR A LISTA)
    # COPY ()
    # FROMKEYS (CRIA CHAVES PARA UM DICIONÁRIO, PODENDO TER VALORES OU NÃO  )
    # GET (BUSCAR VALORES DE UM DICIONARIO, ATRAS DA CHAVE)
    # ITEMS (RETORNA OS PARES CHAVE-VALOR DO DICIONARIO)
    # KEYS (RETORNA AS CHAVES DO DICIONARIO)
    # POP (REMOVE UM VALOR ESPECIFICADO DO DICIONARIO, SE NÃO EXISTE, PODE SER APONTADO UM VALOR COMO RETORNO '{}' COMO RETORNO)
    # POPITEM (REMOVE VALORES NA SEQUÊNCIA)
    # SETDEFAULT ()
    # UPDATE (PERMITE A ATUALIZAÇÃO DE UM DICIONARIO POR NOVO DICIONARIO, QUE PODE TER CONFIGURAÇÃO DISTINTA)
    # VALUES (RETORNA OS VALORES DA CHAVE)
    # IN (VERIFICA A EXISTE DAQUELE VALOR NO DICIONARIO)
    # DEL (REMOVE VALORES DO DICIONARIO)