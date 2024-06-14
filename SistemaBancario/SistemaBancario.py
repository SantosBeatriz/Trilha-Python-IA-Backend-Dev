def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def visualizar_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_cliente(nome, data_nascimento, cpf, endereco):
    return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}

def criar_conta_corrente(numero_conta, usuario):
    return {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario}

def listar_usuarios_e_contas(clientes, contas):
    print("\n=== Lista de Usuários e Suas Contas Correntes ===\n")
    
    for cpf, cliente in clientes.items():
        print(f"Cliente: {cliente['nome']}")
        print(f"CPF: {cpf}")
        print("Endereço:", cliente['endereco'])
        print("Data de Nascimento:", cliente['data_nascimento'])
        print("Contas Correntes:")

        # Verifica se existem contas correntes associadas ao cliente
        contas_cliente = [conta for conta in contas if conta['usuario']['cpf'] == cpf]

        if contas_cliente:
            for conta in contas_cliente:
                print(f" - Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}")
        else:
            print("Nenhuma conta corrente encontrada para este cliente.")
        
        print("=" * 50)

# Inicializando o sistema bancário
clientes = {}
contas = []
numero_conta = 1

menu = """
[u] Criar Usuário
[c] Criar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar Usuários e Contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        visualizar_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        nome = input("Informe o nome do cliente: ")
        data_nascimento = input("Informe a data de nascimento do cliente (dd/mm/aaaa): ")
        cpf = input("Informe o CPF do cliente: ")
        endereco = input("Informe o endereço do cliente (rua, número, bairro, cidade/estado): ")

        if cpf in clientes:
            print("Operação falhou! Já existe um cliente com este CPF.")
        else:
            cliente = criar_cliente(nome, data_nascimento, cpf, endereco)
            clientes[cpf] = cliente
            print("Cliente criado com sucesso!")

    elif opcao == "c":
        cpf = input("Informe o CPF do cliente: ")

        if cpf not in clientes:
            print("Operação falhou! Cliente não encontrado.")
        else:
            usuario = clientes[cpf]
            conta = criar_conta_corrente(numero_conta, usuario)
            contas.append(conta)
            numero_conta += 1
            print("Conta corrente criada com sucesso!")

    elif opcao == "l":
        listar_usuarios_e_contas(clientes, contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")