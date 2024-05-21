"""
        SEPARAR AS FUNÇÕES EXISTENTES DE SAQUE, DEPÓSITO E EXTRATO EM FUNÇÕES. 
        CRIAR DUAS NOVAS FUNÇÕES: CADASTRAR USUÁRIO (CLIEMTE) E CADASTRAR CONTA BANCÁRIA
    """
def menu():
    menu = """\n
    ================ MENU ================
    [d]  - Depositar
    [s]  - Sacar
    [e]  - Extrato
    [nc] - Nova conta
    [lc] - Listar contas
    [nu] - Novo usuário
    [q]  - Sair
    => """
    return input(menu)

menu()