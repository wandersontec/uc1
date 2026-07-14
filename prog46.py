soma = 0

codigo = input("Digite o código do produto (0 para encerrar): ")

while codigo != "0":
    if codigo == "001":
        print("Produto adicionado: Arroz - R$ 4,00")
        soma += 4.00
    elif codigo == "002":
        print("Produto adicionado: Feijão - R$ 7,00")
        soma += 7.00
    elif codigo == "003":
        print("Produto adicionado: Macarrão - R$ 5,00")
        soma += 5.00
    else:
        print("Código inválido!")

    codigo = input("Digite outro código (0 para encerrar): ")

print(f"Total da compra: R$ {soma:.2f}")