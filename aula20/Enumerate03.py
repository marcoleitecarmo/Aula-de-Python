lista = [['Edu', 'João', 'Luiz'],
         ['Maria', 'Aline', 'Joana'],
         ['Helena', 'Edu', 'Luz'],
         ]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][2])
print('=' * 100)

enumerada = list(enumerate(lista))
print(enumerada)
print(enumerada[1][1][2])
print(enumerada[0][1][2])
print(enumerada[2][1][2])
print('=' * 100)

for v1, v2, in enumerate(lista, 53):
    print(v1, v2)
print('=' * 100)

for v1 in enumerate(lista, 53):
    valor_enumerada, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)
print('=' * 100)

for v1 in enumerate(lista, 53):
    valor_enumerada, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)
