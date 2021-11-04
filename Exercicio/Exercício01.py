from datetime import date

data_atual = date.today().year

n = str(input('Digite o nome: '))
a = float(input('Digite a altura: '))
p = float(input('Digite o peso kg: '))
an = int(input('Digite o ano de nascimento: '))

i = data_atual - an
imc = p / a ** 2

print(f'{n} tem {i} anos, {a} de altura e pesa {p:.2f}kg.')
print(f'O IMC de {n} é {imc:.2f}')
print(f'{n} nasceu em {an}')
