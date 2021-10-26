from dados import produtos, pessoas, lista


def idades(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False


nova_lista = filter(idades, pessoas)

for idade in nova_lista:
    print(idade)
