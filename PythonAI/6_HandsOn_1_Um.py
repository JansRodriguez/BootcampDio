menu = """ 
        CRIANDO UM SISTEMA BANCÁRIO
        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Sair
"""
    ## VARIÁVEIS
saldo, numero_saques, numero_deposito = 0
limite_valor_sacado = 500
extrato = ""
LIMITES_SAQUES = 3

while True:
    
    print(menu)
    opcao = int(input("Digite sua opcao: "))

    if opcao == 1:
        depósito = float(input('Informe o valor que desejar depostar: '))

        if depósito <= 0:
            print('Operação inválida. É necessário depositar valores superior a R$ 0,01')
        else:
            numero_deposito += 1
            saldo += depósito
            extrato += f'Depósito: R$ {saldo:.2f}\n'

    elif opcao == 2:
        saque = float(input('Informe o valor a sacar: '))
        
        excedeuLimiteSaques = numero_saques >= LIMITES_SAQUES

        if saque > saldo:   ## saldo_insuficiente
            print('Você não possui saldo suficiente para a operação.')
        elif saque > limite_valor_sacado:   ## excedeuLimite
            print('O limite diário para a operação de saque foi excedido.')
        elif excedeuLimiteSaques:
            print('Você já realizou o máximo de operações diárias de saques.')
        elif saque > 0:
            numero_saques += 1
            saldo -= saque
            extrato += f'Saque: R$ {saque:.2f}\n'
            print('Saque realizado com sucesso!!!')

    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

        print(f'Saldo da conta: R$ {saldo}\nQuantidade de depósito realizado: {numero_deposito}\nQuantidade de saques realizados: {numero_saques}')

    elif opcao == 4:
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")