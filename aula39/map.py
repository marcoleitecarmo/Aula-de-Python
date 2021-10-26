from dados import produtos, pessoa, lista


def aumento_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumento_preco, produtos)

for produto in novos_produtos:
    print(produto)
