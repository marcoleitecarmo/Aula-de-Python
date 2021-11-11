# setter = configurando valor (=)
# setter função de configura um valor

# getter = obter um valor (.)

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


p1 = Pessoa('Otavio')
print(p1.nome)
