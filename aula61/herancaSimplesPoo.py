from classes import *

"""
Associação - Usa | Agregação - Tem | Compósição - É dono | Herança - É
"""

c1 = Cliente('Luiz', 45)
a1 = Aluno('Carlos', 23)

print(c1.nome)
print(a1.nome)
print('#' * 100)
c1.falar()
a1.falar()
print('*' * 100)
c1.comprar()
a1.estudar()
