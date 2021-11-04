"""
For / Else em Python
"""

lista = ['Luiz Otávio', 'Roberto Carlos', 'Mairia Alcione']

for contador in lista:
    if contador.startswith('R'):
        print('Começa com R', contador)
    else:
        print("Não começa com R", contador)
print('-' * 40)

lista = ['Luiz Otávio', 'Roberto Carlos', 'Mairia Alcione']
comeca_com_M = False

for contador in lista:
    if contador.lower().startswith('m'):
        comeca_com_M = True
if comeca_com_M:
    print('Existe uma palavra que começa com M.')
else:
    print('Não existe uma palavra que começa com M.')

print('=' * 40)

lista2 = ['Roberto', 'João', 'Carlos']

for valor in lista2:
    if valor.lower().startswith('j'):
        continue
    print(valor)
