from classes import *

"""
Associação - Usa | Agregação - Tem | Compósição - É dono | Herança - É
"""

c1 = Cliente('Luiz', 23)
c1.comprar()

print()

c2 = ClienteVIP('Rose', 25, 'Miranda')
c2.falar()
