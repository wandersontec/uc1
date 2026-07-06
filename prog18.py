g = input("Digite o gênero (M ou F): ").upper()
i = int(input("Digite a idade: "))
print(f"sexo {g} idade {i}")
if g == "M" and i >= 18:
    print("Apto ao alistamento militar.")
else:
    print("Não apto ao alistamento militar.")