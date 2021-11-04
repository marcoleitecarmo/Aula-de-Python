from itertools import count

"""
Zip - Unindo interáveis
zip une as listas pela menor lista
"""

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro']
estados = ['SP', 'MG', 'BA', 'RJ']

cidades_estados = zip(cidades, estados)
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))

print('$' * 100)

cidades1 = ['Recife', 'Campo Grande', 'Porto Alegre', 'Curitiba']
estados1 = ['CE', 'MS', 'RS', 'PR']
cidades1_estados1 = zip(cidades1, estados1)

for valor in cidades1_estados1:
    print(valor)
print('*' * 100)

cidades2 = ['Recife', 'Campo Grande', 'Porto Alegre', 'Curitiba']
estados2 = ['CE', 'MS', 'RS', 'PR']
cidades2_estados2 = zip(estados2, cidades2)

print(list(cidades2_estados2))
print('&' * 100)

indice = count()
cidades3 = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Sergipe']
estados3 = ['SP', 'RJ', 'MG']

cidades3_estados3 = zip(indice, estados3, cidades3)
for indice, estados3, cidades3 in cidades3_estados3:
    print(indice, estados3, cidades3)
