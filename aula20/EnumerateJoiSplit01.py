"""
Split, Join, Enumerate em Python
*split - Dividir uma string # str
* join - Juntar em lista # str
* enumerate - Enumerar elementos da lista 3 iteráveis
"""
string = 'O Brasil é o o o pais do futebol, o Brasil e penta.'
lista1 = string.split(' ')
lista2 = string.split(',')
print(lista1)
print(lista2)

for valor in lista1:
    print(valor, end=' ')
print()
print('=' * 60)

for valor in lista1:
    print(f'A palavra {valor} {lista1.count(valor)}x na frase. ')

print('=' * 60)

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}X)')
