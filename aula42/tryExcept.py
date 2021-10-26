try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except IndexError as erro:
    print('Erro de indice.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
print('Bora continuar.......')
