dia = int(input("Digite uma opção: "))
match dia:
    case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
        print("Dia da Semana. Dia de Programar!")

    case "Sabado" | "Domingo":
        print("")
