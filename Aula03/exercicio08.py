compra = float(input("Digite o valor da compra: "))

if compra >= 100:
    desconto = compra * 0.10
    valor_final = compra - desconto
    print(f"Sua compra foi de R$ {compra}. Foi aplicado um desconto (10%) de R$ {desconto}, portanto, o valor total a pagar é de R$ {valor_final}")

elif 50 <= compra < 100:
    desconto = compra * 0.05
    valor_final = compra - desconto
    print(f"Sua compra foi de R$ {compra}. Foi aplicado um desconto (5%) de R$ {desconto}, portanto, o valor total a pagar é de R$ {valor_final}")

else:
    print(f"Sua compra foi de R$ {compra}. Não é possível aplicar desconto, portanto, o valor total a pagar é de R$ {compra}")