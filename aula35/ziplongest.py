#  zip_longest une as listas pela maior lista

from itertools import zip_longest, count

indice = count()
cidades3 = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Sergipe']
estados3 = ['SP', 'RJ', 'MG']

cidades3_estados3 = zip_longest(indice, estados3, cidades3, fillvalue='Estado')
for indice, estados, cidades in cidades3_estados3:
    print(indice, estados3, cidades3)
