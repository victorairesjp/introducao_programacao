conta = str(input("Digite sua conta: "))
saldo = float(input("Digite o saldo da conta: "))
credito = float(input("Digite o valor total das receitas: "))
debito = float(input("Digite o valor total das despesas: "))

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print(f"O saldo atual é positivo e é de R$ {saldo_atual:.2f}")
    
else:
    print(f"O saldo atual é negativo e é de R$ {saldo_atual:.2f}")
