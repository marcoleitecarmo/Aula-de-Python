# Compreensão de dicionarios

l1 = [1, 2, 3, 4, 5, 6]
l2 = [v * 2 for v in l1]
l3 = [v * 3 for v in l2]
print(l2)
print(l3)
print('*' * 50)

lista = [
    ('Chave', 'Valor'),
    ('Chave2', 'Valor2')
]
d1 = {x: y for x, y in lista}
d2 = dict(lista)
d3 = {x.upper(): y.upper() for x, y in lista}
print(d1)
print(d2)
print(d3)
print('#' * 50)

d4 = {x for x in range(5)}
print(d4, type(d4))

d5 = {f'chave_{x}': x ** 2 for x in range(5)}
print(d5, type(d5))
