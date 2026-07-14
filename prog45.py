soma = 0
n = int(input("Digite um número (0 para encerrar): "))
while n != 0:
    soma += n
    n = int(input("Digite outro número (0 para encerrar): "))
print("A soma dos números é:", soma)