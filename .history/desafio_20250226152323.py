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
        valor = float(input("Insira o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}/n"
        
        else:
            print 