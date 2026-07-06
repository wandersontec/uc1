# Sistema de votação

print("=== SISTEMA DE VOTAÇÃO ===")
print("Candidatos:")
print("15 - Juquinha")
print("25 - Luizinho")
print("36 - Aninha")

voto = int(input("\nDigite o número do candidato: "))

if voto == 15:
    print("Você votou em Juquinha.")
elif voto == 25:
    print("Você votou em Luizinho.")
elif voto == 36:
    print("Você votou em Aninha.")
else:
    print("Número inválido.")