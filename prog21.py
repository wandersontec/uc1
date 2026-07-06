opcao = int(input("Digite uma opção: "))
match opcao:
    case 1:
        print("Você escolheu a opção 1: Ver Saldo.")

    case 2:
        print("Você escolheu a opção 2: Fazer saque.")

    case 3:
        print("Você escolheu a opção 3: Falar com atendente.")

    case _:
        print("Opção inválida! Escolha um número de 1 a 3.")