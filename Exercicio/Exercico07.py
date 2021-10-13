def olaMundo():
    return 'Ola mundo!'


def mestre(funcao):
    return funcao()


def mestres(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def falaOi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executado = mestres(falaOi, 'Luiz')
executado2 = mestres(saudacao, 'Luiz', saudacao='Bom dia')
print(executado)
print(executado2)

executando = mestre(olaMundo)
print(executando)
