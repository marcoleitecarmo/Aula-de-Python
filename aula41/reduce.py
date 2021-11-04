from dados import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)
print(soma_lista)

print('*' * 100)

soma_preco = reduce(lambda acumulador, produto: produto['preco'] + acumulador, produtos, 0)
print(soma_preco)
print(soma_preco / len(produtos))

print('*' * 100)

soma_idades = reduce(lambda ac, pessoa: ac + pessoa['idade'], pessoas, 0)
print(soma_idades)
print(soma_idades / len(pessoas))
