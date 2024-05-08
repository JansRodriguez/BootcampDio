menu = """ 
        CRIANDO UM SISTEMA BANCÁRIO
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Sair
"""
    ## VARIÁVEIS
saldo = 0
limite = 500
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Depositar")
    elif opcao == 2:
        print("Sacar")
    elif opcao == 3:
        print("Extrato")
    elif opcao == 4:
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")