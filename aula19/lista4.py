lista1 = [5, 30, 12, 1, 14, 19, 51, 9, 47]
print(max(lista1))
print(min(lista1))
print('\033[31m=\033[m' * 30)

lista2 = list(range(1, 10))
print(lista2)
print('\033[31m=\033[m' * 30)

lista3 = list(range(0, 100, 8))

for valor in lista3:
    print(valor, end=' ')
print()
print('\033[31m=\033[m' * 30)
print()

lista4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

soma = 0
for valor in lista4:
    soma += valor
print(soma)
