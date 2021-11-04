"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Carlos', 'André', 'Eduardo', 'Letícia', 'Bruno', 'Rose']

for grupo in combinations(pessoas, 2):
    print(grupo)

print('=' * 100)

pessoas1 = ['Carlos', 'André', 'Eduardo', 'Letícia', 'Bruno', 'Rose']

for grupo1 in permutations(pessoas1, 2):
    print(grupo1)

print('*' * 100)

pessoas2 = ['Carlos', 'André', 'Eduardo', 'Letícia', 'Bruno', 'Rose']

for grupo2 in product(pessoas2, repeat=2):
    print(grupo2)
