menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Valor de R$ {valor:.2f} depositado com sucesso.\nSaldo final: R$ {saldo:.2f}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite por saque. (R$ 500,00)")

        elif excedeu_saques:
            print("Operação falhou! A quantidade diária de saques foi excedida.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} \n"
            numero_saques += 1
            print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso.\nSaldo final: R$ {saldo:.2f}")

        else:
            print("Operação falhou! O Valor informado é inválido.")
    elif opcao == "3":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
