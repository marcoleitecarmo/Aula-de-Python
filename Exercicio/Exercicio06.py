def saudacao(msg, nome):
    print(f'{msg}, {nome}')


def soma(a1, a2, a3):
    print(a1 + a2 + a3)


def aumento(valor, percentual):
    return valor + (valor * percentual / 100)


def fbzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n


from random import randint

for c in range(100):
    aleatorio = randint(0, 100)
    print(fbzz(aleatorio))

ap = aumento(50, 10)
print(ap)
ac = aumento(100, 10)
print(ac)
al = aumento(10, 10)
print(al)
am = aumento(15, 100)
print(am)

soma(2, 1, 3)
soma(1, 1, 1)
soma(2, 1, 1)

saudacao('Ola', 'Joãozinho')
saudacao('Oi', 'Maria')
saudacao('Hey', 'Eduardo')
