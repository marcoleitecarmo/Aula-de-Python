from collections import deque
from time import sleep
"""
Pilhas e filas
Pilha (stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os índices serão modificados
"""
"""
# Pilha

livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')

print(livros)

livro_removido = livros.pop()
print(livros, livro_removido)

"""
"""
# Fila

fila = deque()
fila.append('Joãozinho')
fila.append('Maria')
fila.append('Marco')
fila.append('Luiz')
fila.append('Jose')

print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')


for nome in fila:
    print(nome)

"""
fila = deque(maxlen=5)
fila.extend([1, 2, 3, 4])
fila.append(5)
fila.append(6)
fila.append(7)

print(fila)

print('*' * 50)

fila1 = deque(maxlen=10)

for i in range(50):
    fila1.append(i)
    sleep(0.5)
    print(fila1)

print('#' * 70)

fila2 = deque(maxlen=10)
fila2.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fila2.insert(2, 'Luiz Otávio')
print(fila2)