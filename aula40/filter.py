from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

print('*' * 100)

nova_lista2 = [x for x in lista if x > 5]
print(nova_lista2)

