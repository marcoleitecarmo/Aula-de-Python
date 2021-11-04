#  lists, tuples, str -> Sequencias -> Iterável

nome = 'Marco Antonio'
for letra in nome:
    print(letra, end=' ')

print()
print('#' * 100)

nome1 = 'Roberto Carlos'
iterador = iter(nome1)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print('Se tiver outro next(iterador) vai dar erro de StopIteration')
print('Acabou as letras de nome1 por isto o erro. Usando o for não da erro.')
print(next(iterador))
