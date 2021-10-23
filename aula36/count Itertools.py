"""
count - Itertools
"""
from itertools import count

contador = count()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

print('*' * 100)

contador1 = count(start=5, step=2)
for valor1 in contador1:
    print(valor1)

    if valor1 >= 10:
        break

print('-' * 100)

contador2 = count(start=0, step=-1)
for valor2 in contador2:
    print(round(valor2, 2))

    if valor2 >= 10 or valor2 <= -10:
        break
