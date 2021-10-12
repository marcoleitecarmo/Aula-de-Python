numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    condicao = str(input('Deseja continuar? sim ou não? [S/N] ')).upper().strip()[0]

    if condicao == 'N':
        numeros.sort()
        unicos = list(set(numeros))
        # O comando  list(set(lista))  faz com que os números repetidos digitados não se repitam.
        print(f'Os números digitados (excluindo os duplicados) foram {unicos}')
        break

    elif condicao != 'S':
        # Como faço para fazer o usuário retornar a "condicao" SIM ou NÃO?
        print('Essa opção não existe. Tente de novo.')
