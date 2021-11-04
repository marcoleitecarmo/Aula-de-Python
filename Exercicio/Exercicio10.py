carrinho = [('Produto 1', 30), ('Produto 2', 20), ('Produto 3', 50)]

total = []
for produto in carrinho:
    total.append(produto[1])
print(sum(total))
print('*' * 100)
# Vamos usar list comprehension neste exercício abaixo:

carrinho1 = [('Produto 1', 30), ('Produto 2', 20), ('Produto 3', 50)]

total = sum([float(y) for x, y in carrinho1])
print(carrinho1)
print(total)
