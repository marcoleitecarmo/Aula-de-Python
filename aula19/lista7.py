secreto = 'Brasil'
secreto_temporario = ''

for letra_secreta in secreto:
    if letra_secreta != 's':
        print(letra_secreta, end='')

print()
print('-' * 35)
for letra_secreta in secreto:
    if letra_secreta == 's':
        pass
    else:
        print(letra_secreta, end='')

print()
print('-' * 35)
for letra_secreta in secreto:
    if not letra_secreta == 's':
        print(letra_secreta, end='')
