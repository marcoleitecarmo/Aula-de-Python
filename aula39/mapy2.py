from dados import produtos, pessoas, lista

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
print('*' * 100)


def aumenta_idade(p):
    p['nova_idade'] = p['idade'] + 5
    return p


nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
