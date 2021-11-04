num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print('Você digitou um número par.')
    else:
        print('Você digiotu um número impar.')
else:
    print('Você não digitou um número inteiro')
