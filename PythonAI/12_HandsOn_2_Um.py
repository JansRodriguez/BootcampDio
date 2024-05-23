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
## FUNÇÃO DEPÓSITO - POSITIONAL ONLY
def deposito(saldo, valorDeposito, extrato, numeroDeposito, /):

    if valorDeposito <= 0:
        print(f'O valor R$ {valorDeposito} não é aceitável para depósito.\nPor gentileza, informar um valor válido')
    elif valorDeposito > 0:
        saldo += valorDeposito
        numeroDeposito += 1
        extrato += f'Depósito R$ {saldo:.2f}\n'
        print('Depósito realizado com sucesso!!!')

    return saldo, extrato
## FUNÇÃO EXTRATO - POSITIONAL ONLY E KEYWORD ONLY
    ## ARGUMENTOS POSIONAIS: saldo, 
    ## ARGUMENTOS NOMEADOS: extrato
def extrato(numeroDeposito, numeroDeSaques, saldo, /, *, extrato):
    print("================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

    print("==========================================")
    print(f'Saldo da conta: R$ {saldo}\nQuantidade de depósito realizado: {numeroDeposito}\nQuantidade de saques realizados: {numeroDeSaques}')
## FUNÇÃO PARA VERIFICAR SE EXISTE O USUÁRIO ANTES DE CRIAR USUÁRIOS
def verificarUsuário(cpf, usuarios):
    usuáriosVerificados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuáriosVerificados[0] if usuáriosVerificados else 'Usuário ainda não cadastrado.'
## FUNÇÃO CRIAR USUÁRIOS
def criarUsuarios(usuarios):
    cpf = input("Informe o numero do CPF: ")
    usuario = verificarUsuário(cpf, usuarios)

    if usuario:
        print('Já existe usuário coom esse CPF!!')
        return
    
    nome = input('Informe o noome completo: ')
    dataNascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input("Informe o endereço completo (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        'Nome': nome,
        'Data de Nascimento': dataNascimento,
        'Endereço' : endereco
    }
    )

    print('Usuário cadastrado com sucesso!!!')
## FUNÇÃO PARA CRIAR CONTAS
def criarContas(agencia, numeroDaConta, usuarios):
    cpf = input("Informe o numero do CPF: ")
    usuario = verificarUsuário(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!!!')
        return {
            "Agencia" : agencia,
            "Número da Conta" : numeroDaConta,
            "Usuários" : usuarios
        } 
    print('Usuário não encontrado!!!')
## FUNÇÃO PARA LISTAR AS CONTAS EXISTENTES
def listarContas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t{conta['numeroDaConta']}
            Titular:\t{conta['usuário']['nome']}

"""
        print("="*100)
        print(linha)
## FUNÇÃO PRINCIPAL QUE CHAMARÁ TODAS AS FUNÇÕES CRIADAS ACIMA
def principal():
    ## Na Função principal, precisa conter as váriaveis que serão 'manipuladas' com informações.
        ## VARIÁVEIS
    saldo = 0
    numeroDeSaques = 0
    numeroDeposito = 0
    limiteValor = 500
    extrato = ""
    usuarios = []
    contas = []
        ## CONSTANTES
    LIMITESDESAQUES = 3
    AGENCIA = '0001'

    while True:
        menu()
        opcao = int(input("Digite sua opcao: "))

        if opcao == 1:
            valorDeposito = float(input('Informe o valor que desejar depostar: '))
            saldo, extrato = deposito(saldo, valorDeposito, extrato, numeroDeposito)
        elif opcao == 2:
            valorSaque = float(input('Informe o valor a sacar: '))

            saldo, extrato = saque(
                saldo=saldo,
                valorSaque=valorSaque,
                extrato=extrato,
                limiteValor=limiteValor,
                numeroDeSaques=numeroDeSaques,
                limiteDeSaques=LIMITESDESAQUES
            )
        elif opcao == 3:
            extrato(saldo, extrato=extrato)
        elif opcao == 4:
            numeroDaConta = len(contas) + 1
            conta = criarContas(AGENCIA, numeroDaConta, usuarios)
            if conta:
                conta.append(conta)
        elif opcao == 5:
            listarContas(contas)
        elif opcao == 6:
            criarUsuarios(usuarios)
        elif opcao == 0:
            break
        else:
            print("Operação não listada. Favor, verificar as opções novamente!")
principal()