# Sistema Bancário - Versão 1

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    menu = """

    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==========================
    
    => """

    opcao = input(menu)

    # DEPÓSITO
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("✅ Depósito realizado com sucesso!")
        else:
            print("❌ Operação falhou! O valor informado é inválido.")

    # SAQUE
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor <= 0:
            print("❌ Operação falhou! O valor informado é inválido.")

        elif excedeu_saldo:
            print("❌ Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("❌ Operação falhou! O limite máximo por saque é R$ 500.00.")

        elif excedeu_saques:
            print("❌ Operação falhou! Número máximo de 3 saques diários atingido.")

        else:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print("✅ Saque realizado com sucesso!")

    # EXTRATO
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================")

    # SAIR
    elif opcao == "q":
        print("👋 Obrigado por usar nosso sistema bancário!")
        break

    else:
        print("❌ Operação inválida! Selecione novamente a operação desejada.")
