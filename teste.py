"""
def calcular_media(notas):
    return sum(notas) / len(notas)


def obter_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    return "Reprovado"


for _ in range(4):
    nome = input("Nome do aluno: ")

    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a {i}ª nota: "))
        notas.append(nota)

    media = calcular_media(notas)
    situacao = obter_situacao(media)

    print("\n===== BOLETIM =====")
    print(f"Aluno.....: {nome}")
    print(f"Notas.....: {notas}")
    print(f"Média.....: {media:.2f}")
    print(f"Situação..: {situacao}")
    '''




    