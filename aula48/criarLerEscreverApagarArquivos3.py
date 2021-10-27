# https://docs.python.org/3/lubrary/functions.html#open
# Criar arquivo

with open('abc.txt', 'w+') as file:
    file.write('Escrevendo 1\n')
    file.write('Escrevendo 2\n')
    file.write('Escrevendo 3\n')

    file.seek(0, 0)
    print(file.read())
print('*' * 50)
# Ler arquivo

with open('abc.txt', 'r') as file:
    print(file.read())
print('*' * 50)

# Adicionar no arquivo

with open('abc.txt', 'a+') as file:
    file.write('Escrevendo 4\n')
    file.seek(0)
    print(file.read())

# Apagar arquivo:

import os

os.remove('abc.txt')
