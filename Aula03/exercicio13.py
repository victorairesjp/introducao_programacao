salario = float(input("Digite seu salário mensal: "))

if salario <= 2000:
    print("Você está isento de Imposto de renda")

elif 2000 < salario <= 3500:
    imposto = salario * 0.10
    salario_final = salario - imposto
    print(f"O valor do seu Imposto de Renda é de 10%, ou seja R$ {imposto}, portanto seu salário líquido é de R$ {salario_final}")

else: 
    imposto = salario * 0.15
    salario_final = salario - imposto
    print(f"O valor do seu Imposto de Renda é de 15%, ou seja R$ {imposto}, portanto seu salário líquido é de R$ {salario_final}")