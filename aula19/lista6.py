secreta = 'perfume'
digitadas = []
chances = 5
while True:
    if chances <= 0:
        print('Você Perdeu!!!')
        break
    letra = input('Digite uma letra:')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'UHULLL!!!, a letra "{letra}" pertence a palavra secreta ')
    else:
        print(f'AFFFF!!!, a letra "{letra}" não pertence a palavra secreta')

    secreto_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreta:
        print(f'Que legal, Você Ganhou!!!!{secreto_temporario}')
        break
    else:
        print(f'Você Acertou a palavra secreta: {secreto_temporario}')
        if letra not in secreta:
            chances -= 1
        print(f'Você tem {chances} chances')
        print()
