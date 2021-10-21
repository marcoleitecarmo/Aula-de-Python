from itertools import count

indice = count()
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Sergipe']
estados = ['SP', 'RJ', 'MG']

cidades_estados = zip(indice, estados, cidades)
for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)
