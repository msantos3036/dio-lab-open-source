"""
Sistema Bancário Simplificado (v1)
Operações: depósito, saque e extrato.

Regras:
- Depósitos e saques são registrados e exibidos no extrato.
- Máximo de 3 saques diários.
- Limite de R$ 500,00 por saque.
- Não permite saque sem saldo.

Observação:
- Como é a v1 (apenas 1 usuário), não há agência/conta.
"""

from datetime import date


# ------------------------------
# Regras de negócio / constantes
# ------------------------------
LIMITE_SAQUE = 500.00
LIMITE_SAQUES_DIARIOS = 3


# ------------------------------
# Funções auxiliares
# ------------------------------
def formatar_moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def ler_valor_float(mensagem: str) -> float | None:
    """
    Lê um valor numérico do usuário.
    Retorna None se a entrada for inválida.
    Aceita vírgula ou ponto como separador decimal.
    """
    entrada = input(mensagem).strip().replace(".", "").replace(",", ".")
    try:
        valor = float(entrada)
        return valor
    except ValueError:
        return None


def limpar_tela():
    # Simples (evita dependência de SO). Se quiser, pode substituir por os.system.
    print("\n" * 2)


def obter_data_hoje() -> date:
    return date.today()


# ------------------------------
# Operações
# ------------------------------
def depositar(saldo: float, extrato: list[dict]) -> float:
    valor = ler_valor_float("Informe o valor do depósito: ")
    if valor is None:
        print("❌ Valor inválido. Tente novamente.")
        return saldo

    if valor <= 0:
        print("❌ O valor do depósito deve ser maior que zero.")
        return saldo

    saldo += valor
    extrato.append({"tipo": "DEPÓSITO", "valor": valor, "data": obter_data_hoje()})
    print(f"✅ Depósito realizado: {formatar_moeda(valor)}")
    return saldo


def sacar(
    saldo: float,
    extrato: list[dict],
    saques_hoje: int,
) -> tuple[float, int]:
    if saques_hoje >= LIMITE_SAQUES_DIARIOS:
        print("❌ Limite diário de saques atingido.")
        return saldo, saques_hoje

    valor = ler_valor_float("Informe o valor do saque: ")
    if valor is None:
        print("❌ Valor inválido. Tente novamente.")
        return saldo, saques_hoje

    if valor <= 0:
        print("❌ O valor do saque deve ser maior que zero.")
        return saldo, saques_hoje

    if valor > LIMITE_SAQUE:
        print(f"❌ Limite por saque: {formatar_moeda(LIMITE_SAQUE)}")
        return saldo, saques_hoje

    if valor > saldo:
        print("❌ Saldo insuficiente. Não foi possível realizar o saque.")
        return saldo, saques_hoje

    saldo -= valor
    extrato.append({"tipo": "SAQUE", "valor": -valor, "data": obter_data_hoje()})
    saques_hoje += 1
    print(f"✅ Saque realizado: {formatar_moeda(valor)}")
    return saldo, saques_hoje


def imprimir_extrato(saldo: float, extrato: list[dict]) -> None:
    print("\n" + "=" * 32)
    print("EXTRATO".center(32))
    print("=" * 32)

    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for mov in extrato:
            data_str = mov["data"].strftime("%d/%m/%Y")
            tipo = mov["tipo"]
            valor = mov["valor"]

            if tipo == "DEPÓSITO":
                print(f"{data_str} | {tipo:<8} | +{formatar_moeda(valor)}")
            else:
                print(f"{data_str} | {tipo:<8} |  {formatar_moeda(valor)}")

    print("-" * 32)
    print(f"SALDO ATUAL: {formatar_moeda(saldo)}")
    print("=" * 32 + "\n")


# ------------------------------
# Menu / Controle diário
# ------------------------------
def mostrar_menu() -> str:
    return input(
        """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    ).strip().lower()


def main():
    saldo = 0.0
    extrato: list[dict] = []

    data_atual = obter_data_hoje()
    saques_hoje = 0

    while True:
        # Reseta contador diário se virar o dia
        hoje = obter_data_hoje()
        if hoje != data_atual:
            data_atual = hoje
            saques_hoje = 0

        opcao = mostrar_menu()
        limpar_tela()

        if opcao == "d":
            saldo = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, saques_hoje = sacar(saldo, extrato, saques_hoje)

        elif opcao == "e":
            imprimir_extrato(saldo, extrato)

        elif opcao == "q":
            print("✅ Encerrando o sistema. Até mais!")
            break

        else:
            print("❌ Opção inválida. Selecione uma opção do menu.")


if __name__ == "__main__":
    main()
