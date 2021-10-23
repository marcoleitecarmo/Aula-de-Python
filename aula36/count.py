from itertools import count

contador = count()
lista = ['Luiz', 'João', 'Maria', 'Jose', 'Silva', 'Eduardo']
lista = zip(contador, lista)
print(list(lista))
