num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("\n===== MENU =====")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
opcao = int(input("Escolha uma opção: "))


match opcao:

    case 1:
        resultado = num1 + num2

    case 2:
        resultado = num1 - num2
    case 3:
        resultado = num1 * num2
    case 4:
            resultado = num1 / num2
    case _:
    opcao = 0
print(f"resultado! {opcao}")