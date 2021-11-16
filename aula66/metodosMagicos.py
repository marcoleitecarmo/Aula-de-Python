"""
https://rszalski.github.io/magicmethods/
"""


class A:

    def __init__(self):
        print('Eu sou o __init__')

    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i
        return resultado


a = A()
variavel = a(1, 2, 3, 4, 5)
print(variavel)


