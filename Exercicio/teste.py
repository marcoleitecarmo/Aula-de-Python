numero = []
while True:
    for c in range(0, 21):
        if c % 2 == 0:
            print(c, 'Par')
        else:
            print(c, 'Impar')
    qst = str(input('Quer continuar sim ou não? [S/N]')).upper().strip()[0]
    if qst == 'N':
        break
