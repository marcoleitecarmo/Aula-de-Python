def func(*args, **kwargs):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    print(kwargs['nome'], kwargs['sobrenome'])


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
print(*lista, sep='-')

# func(1, 2, 3, 4, 5)
func(*lista, *lista2, nome='Marco', sobrenome='Antonio')
