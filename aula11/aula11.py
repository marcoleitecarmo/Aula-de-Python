# Condicionais if, elif e else
# Operadores Relacionais: ==, >, >=, <, <=, !=

print(2 == 2)  # Estou perguntando se 2 é igual 2 -  Retorna = Verdadeiro
print(2 > 2)  # Estou perguntando se 2 é maior que 2 -  Retorna = Falso
print(2 >= 2)  # Estou perguntando se 2 é maior ou igual a 2 - Retorna = Verdadeiro
print(2 < 2)  # Estou perguntando se 2 é menor que 2 -  Retorna = Falso
print(2 <= 2)  # Estou perguntando se 2 é menor ou igual a 2 - Retorna = Verdadeiro
print(2 != 2)  # Estou perguntando se 2 é diferente de 2 - Retorna = Falso

# Criando um programa  que informa se usuário pode dirigir ou não:

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade > 18:
    print(f'{nome} você pode Dirigir!!')
else:
    print(f'{nome} você não pode dirigir!!')
