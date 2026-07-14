produtos = {"001": ("Arroz   ", 4.00),"002": ("Feijão  ", 7.00),"003": ("Macarrão", 5.00)}
soma = 0
compras = []
codigo = input("Digite o código do produto (0 para encerrar): ")
while codigo != "0":
    if codigo in produtos:
        nome, preco = produtos[codigo]
        print(f"Produto adicionado: {nome} - R$ {preco:.2f}")
        soma += preco
        compras.append(f"{nome} - R$ {preco:.2f}")
    else:
        print("Código inválido!")
    codigo = input("Digite outro código (0 para encerrar): ")
print("\nProdutos comprados:")
for produto in compras:
    print("-", produto)
print(f"\nTotal da compra com 10%: R$ {soma * 1.1:.2f}")