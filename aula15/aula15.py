"""
Formatando valores com modificadores:
: s - Texto (strings)
: d - Inteiro (int)
: f - Números de ponto flutuante (float)
:.(Número) f - Quantidade de casas decimais (float)
:. (Caracteres) (> ou < ou ^) (Quantidade) (Tipo - s, d ou f)
> - Posicionar as strings a Esquera.
< - Posicionar as strings a Direita.
^ - Posicionar as strings ao centro ou centralizar
"""
nome = 'Marco Antonio'
print(f'{nome:s}')  # Estou dizendo que nome é  uma string.
num = 12
print(f'{12:d}')  # Estou dizendo que num é um inteiro
dec = 2.5
print(f'{dec:f}')  # Estou dizendo que dec é um float
dev = 10 / 3
print(f'{dev:.2f}')  # Estou formatando a divisão dev em duas casas decimais (float)
modelo = 5
print(f'{modelo:*>10}')  # Vamos acrecentar nove * a esquerda e colocar o 5 a direita (10 caracteres)
print(f'{modelo:=<10}')  # Vamos acrecentar nove = a direita e colocar o 5 a esquerda
print(f'{modelo:-^10}')  # Vamos acrecentar nove - e colocar o 5 no centro ou centralizado
