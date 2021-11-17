"""
Animal -> respirar (Classe mãe)
     Lobo(Animal) -> respirar / uivar (herda de animal classe mãe)
     Cachorro(Lobo) -> respirar / uivar / latir (herda de classe animal e lobo e dele mesmo.)
     Herança e de cima para baixo. da Classe mãe para filho e netos
"""

from aula68.classeA.interface import Interface

i1 = Interface()
# i1.metodo_da_interface()
i1.chama_metodo_da_interface()
