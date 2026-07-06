v = float(input("Digite a temperatura : "))

if v < 18:
    print(f"{v} - Frio")
elif v >= 18 and v <= 30:
    print(f"{v} - Agradável")
else:
    print(f"{v} - Calor")