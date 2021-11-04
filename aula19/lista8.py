secreta = 'Paranaguaba'
secreto_temporario = ''
digitadas = ['a', 'n', 'P', 'r', 'g', 'u', 'b']

for letra_secreta in secreta:
    print(f'\033[31mIteração para a letra {letra_secreta}\033[m')

    if letra_secreta in digitadas:
        print(f'\033[32mEba, Eu queria {letra_secreta}\033[m')
        secreto_temporario += letra_secreta
    else:
        print(f'\033[33mEu não queria {letra_secreta}\033[m')
        secreto_temporario += '*'
print()
print(secreto_temporario)

if secreta == secreto_temporario:
    print('Você Ganhou!!!')
