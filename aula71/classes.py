""" Descrição rápida e simples:
Classes proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um novo “tipo”
de objeto, permitindo que novas “instâncias” desse tipo sejam produzidas. Cada instância da classe pode ter atributos
anexados a ela, para manter seu estado. Instâncias da classe também podem ter métodos (definidos pela classe) para
modificar seu estado.

"""


class MinhaClasse:
    """Documentação normal
    Conforme qualquer outra documentação que você tenha usado anteriormente.

    """

    atributo = 1
    atributo2 = 'Valor'

    def __init__(self, texto):
        """Inicializa dados


        :param texto: o texto da classe
        :type texto: str

        """
        self.texto = texto
        self.exibe_texto(texto)

    @staticmethod
    def exibe_texto(texto):
        """
        Método que exibe um texto de 100 caracteres na tela
        :param texto: Um texto de 100 caracteres
        :type texto: str
        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypeError: Se o texto não for uma string
        """
        if not isinstance(texto, str):
            raise TypeError('texto precisa ser uma string.')

        if len(texto) > 100:
            raise ValueError('texto precisa ter 100 caracteres ou menos.')
        return texto
