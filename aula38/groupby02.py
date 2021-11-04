from itertools import groupby, tee

alunos = [
    {'Nome': 'Luiz', 'nota': 'A'},
    {'Nome': 'Lucia', 'nota': 'B'},
    {'Nome': 'Carlos', 'nota': 'A'},
    {'Nome': 'Rui', 'nota': 'C'},
    {'Nome': 'Sandro', 'nota': 'D'},
    {'Nome': 'Luciano', 'nota': 'A'},
    {'Nome': 'Ricardo', 'nota': 'B'},
    {'Nome': 'Luiza', 'nota': 'A'},
    {'Nome': 'Maria', 'nota': 'C'},
    {'Nome': 'Sandra', 'nota': 'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
