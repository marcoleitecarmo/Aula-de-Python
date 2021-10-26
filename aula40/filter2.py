from dados import produtos, pessoas, lista

nova_lista = filter(lambda p: p['preco'] > 50, produtos)
for produto in nova_lista:
    print(produto)
print()
print('*' * 100)


def filtra(produto1):
    if produto1['preco'] > 50:
        produto1['Caro'] = True
    return True


novalista2 = filter(filtra, produtos)

for produto in novalista2:
    print(produto)
