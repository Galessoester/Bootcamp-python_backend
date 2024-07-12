import textwrap
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
import csv

ROOT_PATH = Path(__file__).parent

class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self.index]
            self.index += 1
            return f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero}
                Titular:\t{conta.cliente.nome}
                Saldo:\t\tR${conta.saldo}
            """
        except IndexError:
            raise StopIteration

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        qtd_transacao = conta.historico.transacoes_do_dia()

        if qtd_transacao < 10:
            transacao.registrar(conta)
        else:
            print(qtd_transacao)
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.cpf}')>"

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self._limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif numero_saques >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False
    
    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )
    
    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        hoje = datetime.now().strftime("%d/%m/%Y")
        contador = 0
        for transacao in self._transacoes:
            if transacao['data'].startswith(hoje):
                contador += 1
        return contador
    
class Transacao(ABC):
    @property
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class ClienteNaoEncontrado(Exception):
    pass

class ContaNaoEncontrada(Exception):
    pass

def log_transacao(func):
    def envelope(*args, **kwargs):
        funcao = func(*args, **kwargs)
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ROOT_PATH / "log.txt", "a", newline='', encoding="utf-8") as log:
            log.write(f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. Retornou {funcao}\n")


        print(f"Data e hora: {data_hora}\nTransação: {func.__name__}")
        return funcao
    return envelope

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

def filtrar_cliente():
    cpf = input("Informe o CPF (somente número): ")
    caminho_arquivo = ROOT_PATH / "clientes.csv"
    if caminho_arquivo.exists():
        with open(caminho_arquivo, "r", newline='', encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo)
            for row in reader:
                cpf_cliente, nome, data_nascimento, endereco = row
                if cpf_cliente == cpf:
                    return PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf_cliente, endereco=endereco)
    return None

def recuperar_conta_cliente(cliente):
    caminho_arquivo = ROOT_PATH / "contas.csv"
    if caminho_arquivo.exists():
        with open(caminho_arquivo, "r", newline='', encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo)
            next(reader)  # Pular o cabeçalho
            for row in reader:
                agencia, numero, cpf_cliente, saldo = row
                if cpf_cliente == cliente.cpf:
                    conta = ContaCorrente(numero=numero, cliente=cliente)
                    conta._saldo = float(saldo)
                    return conta
    print("\n@@@ Cliente não possui conta! @@@")
    return None

def informar_cliente_conta(clientes):
    cliente = filtrar_cliente()

    if not cliente:
        raise ClienteNaoEncontrado("\n@@@ Cliente não encontrado! @@@")
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        raise ContaNaoEncontrada("\n@@@ Cliente não possui conta! @@@")
    
    return cliente, conta

@log_transacao
def depositar(clientes, valor):
    try:
        cliente, conta = informar_cliente_conta(clientes)
        
        transacao = Deposito(valor)

        cliente.realizar_transacao(conta, transacao)
    except (ClienteNaoEncontrado, ContaNaoEncontrada) as e:
        print(e)

@log_transacao
def sacar(clientes, valor):
    try:
        cliente, conta = informar_cliente_conta(clientes)
        
        transacao = Saque(valor)

        cliente.realizar_transacao(conta, transacao)
    except (ClienteNaoEncontrado, ContaNaoEncontrada) as e:
        print(e)

@log_transacao
def exibir_extrato(clientes):
    try:    
        cliente, conta = informar_cliente_conta(clientes)

        print("\n================ EXTRATO ================")
        # TODO: atualizar a implementação para utilizar o gerador definido em Historico
        extrato = ""
        tem_transacao = False
        for transacao in conta.historico.gerar_relatorio():
            tem_transacao = True
            extrato += f"\nData: {transacao['data']}\nTipo: {transacao['tipo']}:\nValor: R$ {transacao['valor']:.2f}"

        if not tem_transacao:
            extrato = "Não foram realizadas movimentações"

        print(extrato)
        print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
        print("==========================================")
    except (ClienteNaoEncontrado, ContaNaoEncontrada) as e:
        print(e)

@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente()

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)
    atualizar_arquivo_clientes(clientes)


    print("\n=== Cliente criado com sucesso! ===")

@log_transacao
def criar_conta(numero_conta, contas):
    cliente = filtrar_cliente()

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)
    contas.append(conta)
    cliente.contas.append(conta)

    atualizar_arquivo_contas(conta)

    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in ContaIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def atualizar_arquivo_clientes(clientes):
    with open(ROOT_PATH / "clientes.csv", "a", newline='', encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        for cliente in clientes:
            writer.writerow([cliente.cpf, cliente.nome, cliente.data_nascimento, cliente.endereco])

def atualizar_arquivo_contas(contas):
    with open(ROOT_PATH / "contas.csv", "a", newline='', encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        if isinstance(contas, list):
            for conta in contas:
                writer.writerow([conta.agencia, conta.numero, conta.cliente.cpf, conta.saldo])
        else:
            writer.writerow([contas.agencia, contas.numero, contas.cliente.cpf, contas.saldo])

def carregar_clientes():
    clientes = []
    caminho_arquivo = ROOT_PATH / "clientes.csv"
    if caminho_arquivo.exists():
        with open(caminho_arquivo, "r", newline='', encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo)
            for row in reader:
                cpf, nome, data_nascimento, endereco = row
                cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
                clientes.append(cliente)
    return clientes

def carregar_contas(clientes):
    contas = []
    caminho_arquivo = ROOT_PATH / "contas.csv"
    if caminho_arquivo.exists():
        with open(caminho_arquivo, "r", newline='', encoding="utf-8") as arquivo:
            reader = csv.reader(arquivo)
            for row in reader:
                agencia, numero, cpf_cliente, saldo = row
                cliente = next
                cliente = next((c for c in clientes if c.cpf == cpf_cliente), None)
                if cliente:
                    conta = ContaCorrente(numero=numero, cliente=cliente)
                    conta._saldo = float(saldo)  # Definindo saldo inicial
                    contas.append(conta)
                    cliente.contas.append(conta)
    return contas

def main():
    clientes = carregar_clientes()
    contas = carregar_contas(clientes)

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            depositar(clientes, valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            sacar(clientes, valor)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

main()