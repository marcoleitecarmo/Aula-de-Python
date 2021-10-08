nome = input('Qual seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada')

print('*' * 50)

a = input('Digite seu nome? ')
print(a or 'Você não digitou nada')
