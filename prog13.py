from datetime import datetime
anoa = datetime.now().year
anon= int(input("ano nascimento  "))
idade = anoa - anon
print("Sua idade é ", idade)
if idade >= 65:
    print("idoso")
elif idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")