def ler_arquivo_txt(nome_arquivo):
    lista_itens = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Remove espaços em branco extras e quebra de linha
            item = linha.strip()
            lista_itens.append(item)
    return lista_itens

nome_arquivo = 'arquivos.txt'  # Substitua 'arquivo.txt' pelo nome do seu arquivo
lista_itens = ler_arquivo_txt(nome_arquivo)
print(lista_itens)