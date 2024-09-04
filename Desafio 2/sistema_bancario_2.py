
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

def realizar_deposito(saldo, extrato, valor_deposito, /): # , / = argumentos da esquerda apenas por posição
    
    if valor_deposito > 0: # valor depositado precisa ser maior que zero
        saldo += valor_deposito
        extrato += f"Depósito: \tR$: {valor_deposito:.2f}\n"
        print(f"\nDepósito de R$:{valor_deposito:.2f} Realizado com sucesso!")
    else:
        print("\nValor inválido! Por favor escolha um valor inteiro maior do que zero.")
    
    return saldo, extrato

def realizar_saque(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saque): # *, = argumentos da direita apenas por chave:valor (nomeados)
    if numero_saques < limite_saque: # quantidade de saque diários limitados
        if saldo > 0: # Saldo precisa ser positivo

            print(f"\nLEMBRE-SE: Você só pode sacar 3x por dia com o limite de R$: {limite:.2f}")            

            if valor_saque > 0: # quantidade desejada de saque precisa ser positivo
                    
                if valor_saque <= limite: # saque nao pode ser maior que o limite da conta
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f"Saque: \t\tR$: {valor_saque:.2f}\n"
                    print(f"\nSaque realizado com sucesso! Você sacou R$:{valor_saque:.2f}")
                    print(f"\nVocê já sacou {numero_saques}x hoje!")
                else:
                    print(f"\nVocê nao pode sacar mais do que seu valor limite de R$:{limite:.2f}")
            else:
                print("\nO valor que você está tentando sacar é inválido. Digite um valor maior que zero.")
        else:
            print("\nSaldo insuficiente! Consulte seu extrato para saber seu saldo total.")
    else:
        print("\nLimite diário de saque insuficiente, você só pode sacar três vezes por dia!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
        print("\n ############### EXTRATO ##############")
        print("Nenhuma movimentação detectada." if not extrato else extrato)
        print(f"\nVocê possui R$:{saldo:.2f} em sua conta.")
        print("#######################################")

def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    lista_clientes = []
    lista_contas = []
    numero_conta = 1

    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == "0": # Sair do sistema

            print("\nObrigado por utilizar nosso sistema! Volte sempre!")
            break

        elif opcao == "1": # Opção de cadastrar novos clientes
        
            cadastrar_clientes(lista_clientes)

        elif opcao == "2": #opção de exibir todos so clientes cadastrados

            exibir_clientes(lista_clientes)

        elif opcao == "3": # Opção  de criar nova conta
            conta = criar_conta(AGENCIA, numero_conta, lista_clientes)

            if conta:
                lista_contas.append(conta)
                numero_conta += 1
        
        elif opcao == "4": # Opção de exibir contas cadastradas
        
            exibir_contas(lista_contas)
        
        elif opcao == "5": # Opção de depositar
        
            valor_deposito = float(input("\nQual o valor do deposito? "))
            saldo, extrato = realizar_deposito(saldo, extrato, valor_deposito)

        elif opcao == "6": # Opção de sacar

            valor_saque = float(input("Qual o valor do saque? "))
            saldo, extrato, numero_saques = realizar_saque(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUE,
            )

        elif opcao == "7": # Opção para ver o extrato

            exibir_extrato(saldo, extrato=extrato)

        else:
            print("\nOperação inválida, digite uma opção viável!")

def cadastrar_clientes(lista_clientes):
    cpf = input("\nInforme somente os números do seu CPF: ")
    cliente = verificar_cliente(cpf, lista_clientes)

    if cliente:
        print("\nJá existe um cliente cadastrado com esse cpf!")
        return # Volta para o menu  de opções caso o cpf jah esteja cadastrado
    
    nome = input("\nInforme o nome completo: ")
    data_nascimento = input("\nInforme a data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nInforme o endereço (logradouro, número  da rua - bairro - cidade/sigla do estado): ")

    lista_clientes.append({"cpf":cpf, "nome":nome, "data_nascimento": data_nascimento, "endereco":endereco})

    print("\nCliente cadastrado com sucesso!")

def verificar_cliente(cpf, lista_clientes):
    clientes_verificados = [cliente for cliente in lista_clientes if cliente["cpf"] == cpf] # Verifica se o cpf já está cadastrado
    return clientes_verificados[0] if clientes_verificados else None # Se encontrar retorna o cliente caso contrário retorna None

def criar_conta(agencia, numero_conta, lista_clientes):
    cpf = input("\nInforme somente os números do CPF do cliente: ")
    cliente = verificar_cliente(cpf, lista_clientes)

    if cliente:
        print("\n Conta criada com sucesso!!!")
        return {"agencia":agencia, "numero_conta":numero_conta, "cliente":cliente}
    
    print("\nCliente não encontrado, cadastre o cliente antes de criar uma conta!")

def exibir_contas(lista_contas):
    if not lista_contas:
        print("\nNão há contas cadastradas. Por favor cadastre novas contas!")
    else:
        for conta in lista_contas:
           linha = f"""\
               Agência:\t{conta["agencia"]}
               Número:\t{conta["numero_conta"]}
               Titular:\t{conta["cliente"]["nome"]}
           """
           print(linha)
           print("=" * 50)

def exibir_clientes(lista_clientes):
    if not lista_clientes:
        print("\nNão há clientes cadastrados. Por favor cadastre novos clientes!")
    else:
        for cliente in lista_clientes:
            linha = f"""\
                Nome:\t\t\t{cliente["nome"]}
                CPF:\t\t\t{cliente["cpf"]}
                Data de Nascimento:\t{cliente["data_nascimento"]}
                Endereço:\t\t{cliente["endereco"]}
            """
            print(linha)
            print("=" * 50)

main()