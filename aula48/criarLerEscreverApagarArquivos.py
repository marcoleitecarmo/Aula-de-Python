# https://docs.python.org/3/lubrary/functions.html#open

file = open('abc.txt', 'w+')
file.write('Linha1\n')
file.write('Linha2\n')
file.write('Linha3\n')

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())
file.seek(0, 0)

print('*' * 50)

print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

print('*' * 50)

file.seek(0, 0)
print(file.readlines())
print('*' * 50)
file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')
file.seek(0, 0)
print('*' * 50)
for linha in file:
    print(linha, end='')

file.close()
