quantidade_atual = int(input("Digite a quantidade atual em estoque: "))
quantidade_max = int(input("Digite a quantidade máxima em estoque: "))
quantidade_min = int(input("Digite a quantidade mínima em estoque: "))

quantidade_media = (quantidade_max + quantidade_min) / 2

if quantidade_atual >= quantidade_media:
    print ("Não efetuar compra")

else:
    print("Efetuar compra")