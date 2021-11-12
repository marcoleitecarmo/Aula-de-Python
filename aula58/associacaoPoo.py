# Associção de classes

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('João Amaro')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca)
maquina.escrever()
caneta.escrever()
print('*' * 100)

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

