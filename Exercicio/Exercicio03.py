hora = int(input('Que horas são? (0-23) '))
if 0 <= hora <= 11:
    print('Bom dia!')
elif 12 <= hora <= 17:
    print('Boa tarde!!')
else:
    print('Boa Noite!!!')
