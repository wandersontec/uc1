for i in range(4):
    nome = input("Digite o nome do aluno: ")

    notas = [float(input(f"Digite a {i}ª nota do aluno: ")) for i in range(1, 4)]

# calcule as media dos alunos e verifique a sua situação
    media = sum(notas) / 3

# Saída de dados
    print("\n===== BOLETIM DO ALUNO =====")
    print(f"Aluno: {nome}")
    print(f"Nota do aluno: {notas[2]:.2f}")
    print(f"Média: {media:.2f}")

    # Mensagem final
    print(f"{nome}, sua média é {media:.2f}.")

    #media maior que 7 aprovado
    if media >=7:
        print("aprovado")
    #media entre 5 e 6 recuperação
    elif media >=5 <7:
        print("recuperação")
    #media MENOR que 5 aprovado
    else:
        print("Reprovado")


#NO FINAL MORTRE O NOME DO ALUNO E TODAS AS NOTAS A MEDIA E A situação
