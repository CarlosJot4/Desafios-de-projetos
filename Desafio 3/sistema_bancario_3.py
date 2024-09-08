from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f"""\
            Nome:\t\t{self.nome}
            CPF:\t\t{self.cpf}
            Data de Nascimento:\t{self.data_nascimento}
        """


class Conta:
    
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

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
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nSaldo insuficiente! Consulte seu extrato para saber seu saldo total.")
        elif valor > 0:
            self._saldo -= valor
            print(f"\nSaque realizado com sucesso! Você sacou R$:{valor:.2f}")
            return True
        else:
            print("\nO valor que você está tentando sacar é inválido. Digite um valor maior que zero.")   
        return False
    
    def depositar(self, valor):
        if valor > 0: # valor depositado precisa ser maior que zero
            self._saldo += valor
            print(f"\nDepósito de R$:{valor:.2f} Realizado com sucesso!")
        else:
            print("\nValor inválido! Por favor escolha um valor inteiro maior do que zero.")
            return False
        return True
    

class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        # Pego o tamanho da minha lista do tipo saque
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        execedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if execedeu_limite:
            print(f"\nVocê nao pode sacar mais do que seu valor limite de R$:{self.limite:.2f}")

        elif excedeu_saques:
            print(f"\nLimite diário de saque insuficiente, você só pode sacar {self.limite_saques} vezes por dia!")

        else: #chamo o método sacar da minha classe pai (Conta)
            return super().sacar(valor)

        return False

    def __str__(self) -> str:
        return f"""\
            Agência:\t{self.agencia}
            Conta:\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    # Adiciona uma transação na minha lsita como um dicionário
    def adicionar_transacao(self, transacao):
        mascara_ptbr = "%d/%m/%Y %H:%M"
        data_formatada = datetime.now().strftime(mascara_ptbr) 
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": data_formatada,
            }
        )


class Transacao(ABC):
    
    @abstractmethod
    def registrar(self, conta):
        pass

    @property
    @abstractmethod
    def valor(self):
        pass


class Deposito(Transacao):
    
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)


def menu():
    menu = """
    ------ SISTEMA BANCÁRIO SIMPLES ------
    >>> Escolha uma das opções abaixo <<<

    [1] Novo Cliente
    [2] Mostrar clientes
    [3] Nova Conta
    [4] Mostrar contas
    [5] Depositar
    [6] Sacar
    [7] Extrato
    [0] Sair

    """
    return input(menu)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "0": # Sair do sistema
            print("\nObrigado por utilizar nosso sistema! Volte sempre!")
            break

        elif opcao == "1": # Opção de cadastrar novos clientes
            criar_cliente(clientes)

        elif opcao == "2": #opção de exibir todos so clientes cadastrados
            listar_clientes(clientes)

        elif opcao == "3": # Opção  de criar nova conta
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        
        elif opcao == "4": # Opção de exibir contas cadastradas
            listar_contas(contas)
        
        elif opcao == "5": # Opção de depositar
            depositar(clientes)

        elif opcao == "6": # Opção de sacar
            sacar(clientes)

        elif opcao == "7": # Opção para ver o extrato
            exibir_extrato(clientes)

        else:
            print("\nOperação inválida, digite uma opção viável!")

def depositar(clientes):
    cliente = pedir_cpf(clientes)
    
    valor = float(input("\nInforme o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cliente = pedir_cpf(clientes)

    valor = float(input("\nInforme o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

#pede o cpf e verifica se jah existe algum cliente cadastrado com esse cpf e retorna o cliente com o cpf
def pedir_cpf(clientes):
    cpf = input("\nInforme o CPF do cliente: ")

    cliente = verificar_cliente(cpf, clientes) # para ver se existe o cliente
    if not cliente:
        print("\n Cliente não encontrado!!")
        return

    return cliente

def exibir_extrato(clientes):
    cliente = pedir_cpf(clientes)
    if not cliente:
        print("Nenhuma movimentação encontrada!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("Nenhuma movimentação encontrada!")
        return
    
    print("\n############### EXTRATO ###############")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        print("\nNenhuma movimentação detectada.")
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao["tipo"]}:   \tR${transacao["valor"]:.2f}"

    print(extrato)
    print(f"\nVocê possui R$:{conta.saldo:.2f} em sua conta.")
    print("#######################################")

def criar_conta(numero_conta, clientes, contas):
    cliente = pedir_cpf(clientes)
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n Conta criada com sucesso!!!")

def listar_contas(contas):
    if not contas:
        print("\nNão há contas cadastradas. Por favor cadastre novas contas!")
    else:
        for conta in contas:
          linha = str(conta)
          print(linha)
          print("=" * 50)

def criar_cliente(clientes):
    cpf = input("\nInforme somente os números do seu CPF: ")
    cliente = verificar_cliente(cpf, clientes)

    if cliente:
        print("\nJá existe um cliente cadastrado com esse cpf!")
        return # Volta para o menu  de opções caso o cpf jah esteja cadastrado
    
    nome = input("\nInforme o nome completo: ")
    data_nascimento = input("\nInforme a data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nInforme o endereço (logradouro, número  da rua - bairro - cidade/sigla do estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("\nCliente cadastrado com sucesso!")

def listar_clientes(clientes):
    if not clientes:
        print("\nNão há clientes cadastrados. Por favor cadastre novos clientes!")
    else:
        for cliente in clientes:
          linha = str(cliente)
          print(linha)
          print("=" * 50)

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não encontrado!!!")
        return
    #pega sempre a primeira conta do cliente, para simplificar (caso contrário teria de pedir o numero da conta também)
    return cliente.contas[0] 

def verificar_cliente(cpf, lista_clientes):
    clientes_verificados = [cliente for cliente in lista_clientes if cliente.cpf == cpf] # Verifica se o cpf já está cadastrado
    return clientes_verificados[0] if clientes_verificados else None # Se encontrar retorna o cliente caso contrário retorna None

main()