# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

from sys import platform as so
from random import randint

print(so)
print('*' * 50)

for i in range(10):
    print(randint(0, 10), end=', ')
