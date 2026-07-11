numero = int(input("Digite um número para ver a tabuada: "))
print(f"\nTabuada do {numero}")
y=0
while y<10:
    y=y+1
    print(f"{numero} x {y} = {numero * y}")