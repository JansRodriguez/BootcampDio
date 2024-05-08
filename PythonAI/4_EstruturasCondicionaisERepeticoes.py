## INDENTAÇÃO E BLOCOS
""" 
Com a indentação o interpretador consegue determinar onde um bloco de comando inicia e ele termina.

def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("valor sacado")
sacar(100)
"""
## ESTRUTURAS CONDICIONAIS
""" 
## IF
saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print('Saque realizado com sucesso.')
if saldo < saque:
    print("Sem saldo para o saque.")
"""
## IF - ELIF - ELSE
"""
opcao = int(input("Informe uma opção: \n[1] Sacar \n[2] Extrato\n "))
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo extrato...")
else:
    print("Opção inválida!!")
"""
##ESTRUTURAS DE REPETIÇÃO
"""
## SÃO ESTRUTURAS UTILIZADAS PARA REPETIR UM TRECHO DE CÓDIGO UM DETERMINADO NÚMERO DE VEZES, ESSE NÚMERO PODE SER CONHECDIO PREVIAMENTE OU DETERMINADO ATRAVÉS DE UMA EXPRESSÃO LÓGICA
    ## - FOR
##USADO PARA PERCORRER UM OBJETO ITERÁVEL. QUANDO SABEMOS A EXTA QUANTIDADE DE REPETIÇÕES DE UM BLOCO DE CÓDIGO, OU UM OBJETO ITERÁVEL.
texto = input("Digite um frase qualquer: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
"""
        ## FOR - ELSE
"""
texto = input("Digite um frase qualquer: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")
"""
## - FOR E A FUNÇÃO BUILT-IN RANGE
"""
    # A função range, possui os argumentos [start, stop[, step]]
for numero in range(10):
    print(numero, end=" ")

for numero in range(0, 51, 5):
    print(numero, end=" ")
"""
    ## WHILE
"""
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[3] Sair:\n "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")

        ## WHILE - BREAK
while True:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break
        
        ## WHILE - CONTINUE
        (Quando quisermos pular algum valor.)
    """
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    if numero % 2 == 0:
        continue
    print(numero)