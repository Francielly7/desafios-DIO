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
            extrato += f"Depósito: R$ {valor:.2f}/n"
        
        else:
            print("Valor informado inválido!") 
    
    elif opcao == 2:
        valor = float(input("Insira valor para saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        
        if excedeu_saldo:
            print("Voc~e")
        