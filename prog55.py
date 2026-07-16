def media(a, b, c, d):
    return (a + b + c + d) / 4

notas = [float(input(f"Digite a {i}ª nota bimestral: ")) for i in range(1, 5)]
media = media(notas[0], notas[1], notas[2], notas[3])

if media >= 7:
    print("Aprovado")
elif media >= 5 and media <= 6:
    print("Recuperação")
else:
    print("Reprovado")

nome = input("Digite o nome do aluno: ")

print(f"Aluno: {nome}")
print(f"Média: {media:.2f}")
print(f"{nome}, sua média é {media:.2f}.")

