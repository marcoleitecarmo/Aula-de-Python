valor = 50.00
minutos = int(input('Digite quantos minutos: '))

if minutos > 100:
    pago = (minutos - 100) * 2 + valor

else:
    pago = valor

print(f'Valor a pagar R$ {pago:.2f}')
