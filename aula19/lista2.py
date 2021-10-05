lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
lista4 = lista1 + lista2
lista5 = ['A', 'B', 'C']

lista1.extend(lista2)
lista2.insert(0, 'Banana')
lista3.extend('a')
lista5.append(10)

print(lista1)
print('-' * 30)
print(lista2)
print(lista2[0])
print('-' * 30)
print(lista3)
print('-' * 30)
print(lista4)
print('-' * 30)
print(lista5)
print('-' * 30)
print(lista5[3])
