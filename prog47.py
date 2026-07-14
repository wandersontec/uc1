soma = 0
n = int(input("Digite um número (0 para encerrar): "))
while n != 0:
    soma += n
    n = int(input("Digite outro número (0 para encerrar): "))
print(f"A soma com dos números é:{soma:.2f}")
print(f"A soma com 10% dos números é:{soma * 1.1 :.2f}")