# ==========================
# SISTEMA BANCÁRIO - V2
# ==========================

AGENCIA_PADRAO = "0001"


def filtrar_usuario(cpf, usuarios):
    """Retorna o usuário (dict) se existir, senão None."""
    cpf = "".join([c for c in cpf if c.isdigit()])
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_usuario(usuarios):
    cpf = "".join([c for c in input("CPF (somente números): ") if c.isdigit()])
    if filtrar_usuario(cpf, usuarios):
        print("❌ Já existe usuário com esse CPF.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")

    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (sigla): ")

    endereco = f"{logradouro}, {numero}, {bairro}, {cidade}/{estado}"

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )

    print("✅ Usuário criado com sucesso!")


def criar_conta_corrente(agencia, numero_conta, usuarios, contas):
    cpf = "".join([c for c in input("Informe o CPF do usuário: ") if c.isdigit()])
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("❌ Usuário não encontrado. Cadastre o usuário primeiro.")
        return

    contas.append(
        {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
        }
    )
    print("✅ Conta criada com sucesso!")


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print(
            f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}"
        )


def depositar(saldo, valor, extrato, /):
    """Depósito: argumentos apenas por posição (positional-only)."""
    if valor <= 0:
        print("❌ Operação falhou! Valor inválido.")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print("✅ Depósito realizado com sucesso!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Saque: argumentos apenas por nome (keyword-only)."""
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if valor <= 0:
        print("❌ Operação falhou! Valor inválido.")

    elif excedeu_saldo:
        print("❌ Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print(f"❌ Operação falhou! O limite máximo por saque é R$ {limite:.2f}.")

    elif excedeu_saques:
        print("❌ Operação falhou! Número máximo de saques diários atingido.")

    else:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    """Extrato: saldo por posição, extrato por nome."""
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==============================\n")


def menu():
    return """
========== MENU ==========
[u] Criar usuário
[c] Criar conta corrente
[l] Listar contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==========================
=> """


def main():
    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    limite_saques = 3

    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = input(menu()).lower()

        if opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            criar_conta_corrente(AGENCIA_PADRAO, numero_conta, usuarios, contas)
            # Só incrementa se a conta foi criada de fato (isto é, se existe conta com esse número)
            if contas and contas[-1]["numero_conta"] == numero_conta:
                numero_conta += 1

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "d":
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("👋 Obrigado por usar o sistema bancário!")
            break

        else:
            print("❌ Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
