# https://docs.python.org/3/lubrary/functions.html#open

try:
    file = open('abc.txt', 'w+')
    file.write('Escrevendo')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()
