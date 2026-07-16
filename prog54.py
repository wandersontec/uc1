def idade(anoa, anon):
    return anoa - anon

anoa = 2026

anon = int(input("Ano de nascimento: "))

idade = idade(anoa, anon)

print("Sua idade é", idade)

if idade >= 65:
    print("Idoso")
elif idade >= 18 and idade <65:
    print("Maior de idade")
else:
    print("Menor de idade")