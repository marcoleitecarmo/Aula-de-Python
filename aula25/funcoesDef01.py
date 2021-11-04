"""
Funções - def em Python (Parte 1)
"""


def soma(a, b: object):
    x = a + b
    print(x)
    return x


def maior(a=0):
    while True:
        a = int(input('Digite sua idade: '))
        if a >= 21:
            print('Você é de maior')
        else:
            print('Você é de menor')
        b = input('Quer continuar [S/N]').upper().strip()[0]
        if b == 'N':
            break


# Programa Principal


soma(10, 25)
maior()
