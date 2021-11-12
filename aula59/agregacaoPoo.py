from classe import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneca', 15)
p4 = Produto('Livro', 75)
p5 = Produto('Caderno', 30)

carrinho.inseir_produto(p1)
carrinho.inseir_produto(p2)
carrinho.inseir_produto(p3)
carrinho.inseir_produto(p4)
carrinho.inseir_produto(p5)

carrinho.lista_produto()
print(carrinho.soma_total())
