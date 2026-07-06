# Programa para calcular salário líquido com base no cargo

# Tabela de cargos e salários
cargos = {
    "CAIXA": 1500,
    "VENDEDOR": 2400,
    "GERENTE": 4000
}

# Entrada do usuário
cargo = input("Digite o cargo (CAIXA, VENDEDOR ou GERENTE): ").upper()

# Verifica se o cargo existe
if cargo in cargos:
    salario = cargos[cargo]

    # Cálculo do INSS (12%)
    inss = salario * 0.12

    # Cálculo do IRRF
    if salario > 2000:
        irrf = salario * 0.14
    else:
        irrf = salario * 0.08

    # Salário final
    salario_final = salario - inss - irrf

    # Exibição dos resultados
    print("\n===== HOLERITE =====")
    print(f"Cargo: {cargo}")
    print(f"Salário Bruto: R$ {salario:.2f}")
    print(f"INSS (12%): R$ {inss:.2f}")
    print(f"IRRF: R$ {irrf:.2f}")
    print(f"Salário Líquido: R$ {salario_final:.2f}")
else:
    print("Cargo inválido!")