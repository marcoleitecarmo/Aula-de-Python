lista = [0, 1, 2, 3, 4, 5]
print(hasattr(lista, '__iter__'))
for v in lista:
    print(v)
print('=' * 50)

lista2 = [0, 1, 2, 3, 4, 5]
lista2 = iter(lista2)

print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print(next(lista2))
print()
print(hasattr(lista2, '__next__'))
