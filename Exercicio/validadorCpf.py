while True:
    cpf = input('Digite um CPF: ')
    n_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(n_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            n_cpf += str(d)
    sequencia = n_cpf == str(n_cpf[0]) * len(cpf)

    if cpf == n_cpf and not sequencia:
        print('CPF Válido')
    else:
        print('CPF Inválido')
