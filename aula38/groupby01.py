from itertools import groupby

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
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(len(aluno))

    print()
