"""
        SEPARAR AS FUNÇÕES EXISTENTES DE SAQUE, DEPÓSITO E EXTRATO EM FUNÇÕES. 
        CRIAR DUAS NOVAS FUNÇÕES: CADASTRAR USUÁRIO (CLIEMTE) E CADASTRAR CONTA BANCÁRIA
    """
def menu():
    menu = """
    ================ MENU ================
    [1]  -  Depositar
    [2]  -  Sacar
    [3]  -  Extrato
    [4]  -  Nova conta
    [5]  -  Listar contas
    [6]  -  Novo usuário
    [0]  -  Sair
    """
    return input(menu)

## FUNÇÃO SAQUE - KEYWORDS ONLY
def saque(*, saldo, valorSaque, extrato, limiteValor, numeroDeSaques, limiteDeSaques):

    saldoInsuficiente = saldo < valorSaque
    excedeuLimite = limiteValor < valorSaque
    excedeuSaques = limiteDeSaques <= numeroDeSaques

    if saldoInsuficiente:
        print(' ⚠️ ⚠️ ⚠️ Você não possui saldo suficiente para a operação.')
    elif excedeuLimite:
        print('⚠️ ⚠️ ⚠️ O limite diário para a operação de saque foi excedido.')
    elif excedeuSaques:
        print('⚠️ ⚠️ ⚠️ Você já realizou o máximo de operações diárias de saques.')
    elif saldo > 0:
        saldo -= valorSaque
        numeroDeSaques += 1
        extrato += f'Saque: R$ {valorSaque:.2f}'
        print('Saque realizado com sucesso!!!')
    else:
        print('Operação inválida. É necessário depositar valores superior a R$ 0,01')
        
    return saldo, extrato