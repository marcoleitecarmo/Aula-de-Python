x = 10
y = 'Luiz'

# Trocar valor entre variáveis em outro programas

z = x
x = y
y = z

print(f' x = {x} e y = {y}')
print('-' * 40)

# Troca de valores entre variáveis em Python

a = 20
b = 'Pedro'

a, b = b, a

print(f' a = {a} e b = {b}')
print('=' * 40)

r = 30
s = 'Ricardo'
t = 'Otavio'

r, s, t = t, r, s

print(f' r = {r}, s = {s} e t = {t}')
