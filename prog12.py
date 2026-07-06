nome = input("Digite o nome do aluno: ")

notas = [float(input(f"Digite a {i}ª nota bimestral: ")) for i in range(1, 8)]

# Cálculo da média
media = sum(notas) / 4

# Saída de dados
print("\n===== BOLETIM DO ALUNO =====")
print(f"Aluno: {nome}")
print(f"3ª nota bimestral: {notas[2]:.2f}")
print(f"Média: {media:.2f}")

# Mensagem final
print(f"{nome}, sua média é {media:.2f}.")

if media >=6:
    print("aprovado")
else:
    print("Recuperação")