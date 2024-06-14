from datetime import datetime
import textwrap

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao:
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        raise NotImplementedError

class Deposito(Transacao):
    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(f"Depósito: R$ {self.valor:.2f} em {datetime.now()}")
        return True

class Saque(Transacao):
    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque: R$ {self.valor:.2f} em {datetime.now()}")
            return True
        else:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False

class Conta:
    def __init__(self, cliente, numero):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def saldo(self):
        return self.saldo

    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        transacao = Saque(valor)
        return transacao.registrar(self)

    def depositar(self, valor):
        transacao = Deposito(valor)
        return transacao.registrar(self)

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(nome, data_nascimento, cpf, endereco)

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

# Funções do menu

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    if cpf in usuarios:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = PessoaFisica(nome, data_nascimento, cpf, endereco)
    usuarios[cpf] = usuario

    print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = usuarios.get(cpf)

    if usuario:
        conta = ContaCorrente(usuario, numero_conta)
        usuario.adicionar_conta(conta)
        print("\n=== Conta criada com sucesso! ===")
        return conta
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta.historico.transacoes:
            print(transacao)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")

# Função principal

def main():
    usuarios = {}
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            cpf = input("Informe o CPF do titular da conta: ")
            usuario = usuarios.get(cpf)

            if usuario:
                conta = usuario.contas[0]  # Assumindo que o usuário tem apenas uma conta
                conta.depositar(valor)
            else:
                print("\n@@@ Usuário não encontrado! @@@")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            cpf = input("Informe o CPF do titular da conta: ")
            usuario = usuarios.get(cpf)

            if usuario:
                conta = usuario.contas[0]  # Assumindo que o usuário tem apenas uma conta
                conta.sacar(valor)
            else:
                print("\n@@@ Usuário não encontrado! @@@")

        elif opcao == "e":
            cpf = input("Informe o CPF do titular da conta: ")
            usuario = usuarios.get(cpf)

            if usuario:
                conta = usuario.contas[0]  # Assumindo que o usuário tem apenas uma conta
                exibir_extrato(conta)
            else:
                print("\n@@@ Usuário não encontrado! @@@")

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta("0001", numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
