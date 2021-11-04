string = "O Brasil é penta."
lista = string.split(' ')
string2 = ' '.join(lista)

print(string)
print(lista)
print(string2)
print('=' * 40)

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])
print('*' * 40)

lista = [[1, 2], [3, 4], [5, 6]]

for v in lista:
    print(v)
    print(v[0], v[1])
print('=' * 40)

lista2 = [[0, 'Luiz'], [1, 'João'], [2, 'Maria']]

for indice, nome, in lista2:
    print(indice, nome)
print('/' * 40)

lista3 = ['Luiz', 'João', 'Maria']

for indice2, nome in enumerate(lista3):
    print(indice2, nome)
