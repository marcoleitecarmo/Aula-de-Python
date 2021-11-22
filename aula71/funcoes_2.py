"""
Opcionalmente, a primeira linha do corpo da função pode ser uma literal string, cujo propósito é documentar a função.
Se presente, essa string chama-se docstring. (Há mais informação sobre docstrings na seção Strings de documentação.)
Existem ferramentas que utilizam docstrings para produzir automaticamente documentação online ou para imprimir, ou
ainda, permitir que o usuário navegue interativamente pelo código. É uma boa prática incluir sempre docstrings em suas
funções, portanto, tente fazer disso um hábito.
"""

variavel_1 = 'valor 1'


def soma(x, y):
    """
    Soma x e y

    :param x: primeiro número
    :param y: segundo número
    :return: a soma de x e y
    """
    return x + y


def mutiplica(x, y,  z=None):
    """Mutiplica x, y, z

    Mutiplica x, y e z. O programador por omitir a variável z cado não tenha necessidade de usá-la.
    """
    if z:
        return x * y
    else:
        return x * y * z


variavel_2 = 'valor 2'
variavel_3 = 'valor 3'
variavel_4 = 'valor 4'