
menu = """
------ SISTEMA BANCÁRIO SIMPLES ------
>>> Escolha uma das opções abaixo <<<

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "0": # Sair do sistema

        print("\nObrigado por utilizar nosso sistema! Volte sempre!")
        break

    elif opcao == "1": # Opção de depositar
        
        valor_deposito = float(input("\nQual o valor do deposito? "))

        if valor_deposito > 0: # valor depositado precisa ser maior que zero
            saldo += valor_deposito
            extrato += f"Depósito - R$: {valor_deposito:.2f}\n"
            print(f"\nDeposito de R$:{valor_deposito:.2f} Realizado com sucesso!")
        else:
            print("\nValor inválido! Por favor escolha um valor inteiro maior do que zero.")

    elif opcao == "2": # Opção de sacar

        if numero_saques < LIMITE_SAQUE: # quantidade de saque diários limitados
            if saldo > 0: # Saldo precisa ser positivo

                print(f"\nVocê só pode sacar 3x por dia com o limite de R$: {limite}")
                valor_saque = float(input("Qual o valor do saque? "))

                if valor_saque > 0: # quantidade desejada de saque precisa ser positivo
                    
                    if valor_saque <= limite: # saque nao pode ser maior que o limite da conta
                        saldo -= valor_saque
                        numero_saques += 1
                        extrato += f"Saque - R$: {valor_saque:.2f}\n"
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

    elif opcao == "3": # Opção para ver o extrato

        print("\n ############### EXTRATO ##############")
        print("Nenhuma movimentação detectada." if not extrato else extrato)
        print(f"\nVocê possui R$:{saldo:.2f} em sua conta.")
        print("#######################################")

    else:
        print("\nOperação inválida, digite uma opção viável!")
