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
            print("Operação falhou! Você não tem saldo suficiente")
               
        elif excedeu_limite:
            print("Operação falhou! Você excedeu seu limite diário")
            
        elif excedeu_saques:
            print("Operação falhou! Você excedeu o número de saques!")    
        else:
            print("Operação Inválida!")    
            
    elif opcao == 3:
        print("========== EXTRATO ==========")
        print("Não foram realizadas movimneaç")
             