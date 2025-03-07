menu = """

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Insira o valor para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: R$ {valor:.2f}"

        else:
            print("Valor informado inválido!")

    elif opcao == 2:
        valor = float(input("Insira valor para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou! Você excedeu seu limite diário")

        elif excedeu_saques:
            print("Operação falhou! Você excedeu o número de saques!")

        elif valor > 0:
            saldo -= valor
            extrato += f"\nsaque R${valor:.2f}"
            numero_saques += 1

        else:
            print("Operação Inválida!")

    elif opcao == 3:
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimenações." if not extrato else extrato)
        print(f"\nSaldo R$ {saldo :.2f}")
        print("=============================")

    elif opcao == 4:
        break

    else:
        print("Operação falhou! Digite a opção que deseja!")