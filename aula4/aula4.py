"""
Tipos de dados
str - string - textos 'Assim' e "Assim"
int - inteiro - números inteiros 123456 0 -10 -20 -50 - 60 -1500 1500
float = real/ponto flutuante - números com separado ponto 2.5, -10.9, 20.50
bool = booleano/lógico - True e False = verdadeiro e falso - 10 == 10 = True, 10 != 10 = False
"""
print('Olavo', type('Olavo'))
print(123, type(123))
print(2.5, type(2.5))
print(10 == 10, type(10 == 10))
print(10 != 10, type(10 != 10))
print('-=' * 15)
# Coversão de dados
print('Luiz', type('Luiz'), bool('Luiz'))
print('10', type('10'), type(int('10')))
