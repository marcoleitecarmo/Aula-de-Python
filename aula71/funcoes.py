""" Documentação de Funções
Python é uma linguagem fácil de aprender e poderosa. Ela tem estruturas de dados de alto nível eficientes e uma
abordagem simples mas efetiva de programação orientada a objetos. A elegância de sintaxe e a tipagem dinâmica de
Python aliadas com sua natureza interpretativa, o fazem a linguagem ideal para programas e desenvolvimento de
aplicações rápidas em diversas áreas e na maioria das plataformas.
"""

variavel_1 = 'valor 1'


def soma(x, y):
    """Soma x e y"""
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