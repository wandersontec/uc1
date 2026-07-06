g = input("Você tem ingresso (S ou N): ").upper()
i = int(input("Digite a idade: "))
print(f"Ingresso: {g} | Idade: {i}")
if g == "S" and i >= 12:
    print("Acesso Liberado! Divirta-se no brinquedo.")
elif g == "S" and i < 12:
    print("Você tem ingresso, mas não tem a idade mínima de 12 anos.")
else:
    print("Acesso negado. Você precisa de ingresso.")
