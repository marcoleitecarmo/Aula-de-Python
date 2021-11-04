logged_user = False
if logged_user:
    msg = 'Úsuario logado.'
else:
    msg = 'Úsuario precisa logar.'

print(msg)
print('/' * 40)

# Usando operador ternário em Python

logger_users = True
msg = 'Úsuario logado.' if logger_users else 'Úsuario precisa logar'
print(msg)
print('#' * 40)

idade = input('Qual a sua idade? ')
if not idade.isnumeric():
    print('Você precisa digitar números')
else:
    idade = int(idade)
    de_maior = (idade >= 18)
    msg = 'PODE ACESSAR' if de_maior else 'NÃO PODE ACESSAR.'
    print(msg)
