## Calculadora de IMC

# Entrada de dados
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
# Cálculo do IMC
imc = peso / (altura ** 2)
# Saída
print(f"Seu IMC é: {imc:.2f}")