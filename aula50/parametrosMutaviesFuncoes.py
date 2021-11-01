# Mutável: Listas, dicionários
# Imutavél : Tuplas, strings, números, True, False, none


def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['Jose'])

print(clientes1)
print(clientes2)
