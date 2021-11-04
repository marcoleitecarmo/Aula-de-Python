from dados import produtos, pessoa, lista

nova_lista = map(lambda x: x * 2, lista)
print(lista)
print(list(nova_lista))
print('*' * 100)
nova_lista2 = [x * 2 for x in lista]
print(nova_lista2)
