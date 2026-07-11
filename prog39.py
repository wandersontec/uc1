carros = {}

for i in range(2):
    carro = input("Carro: ")
    marca = input("Fabricante: ")
    valor = float(input("Valor do carro: "))
    carros[carro] = {
        "marca": marca,
        "valor": valor
    }
print(f"lista de carros{carros}")