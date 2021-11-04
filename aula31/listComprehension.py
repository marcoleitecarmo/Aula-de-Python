# Compreensões de listas

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]
l3 = [v * 2 for v in l1]
l4 = [(v, v2) for v in l1 for v2 in range(3)]
l5 = ['Luiz', 'Mauro', 'Maria']
ex1 = [v.replace('a', '@').upper() for v in l5]
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex2 = [(x, y) for x, y in tupla]
ex3 = [(y, x) for x, y in tupla]
ex4 = dict(ex3)

print(l2)
print(l3)
print(l4)
print(ex1)
print(ex2)
print(ex3)
print(ex4['valor2'])
