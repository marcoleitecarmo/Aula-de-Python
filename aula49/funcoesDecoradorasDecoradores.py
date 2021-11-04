def master(funcao):
    def slave(*args, **kwargs):
        print('Estou decorada')
        funcao(*args, **kwargs)

    return slave


@master
def fala_oi():
    print('Oi')


@master
def outra_funcao(msg):
    print(msg)


outra_funcao('Ola, sou Luiz.')
