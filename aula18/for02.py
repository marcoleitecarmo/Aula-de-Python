for numero in range(0, 100, 8):
    print(numero, end=' ')

print()
print('-' * 40)

for n in range(100):
    if n % 8 == 0:
        print(n, end=' ')
print()
print('-' * 40)
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
