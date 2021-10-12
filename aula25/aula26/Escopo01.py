variavel = 'valor'


def func() -> object:
    print(variavel)


def func2():
    global variavel
    variavel = 'Outro valor'
    print(variavel)


func()
func2()

print(variavel)
