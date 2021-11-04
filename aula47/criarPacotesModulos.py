import vendas
from vendas.precos import aumento, reducao
from vendas.formata import fpreco as form

preco = 49.90
preco_com_aumento = aumento(preco, 15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(preco, 15, formata=True)
print(preco_com_reducao)

print(form.real(59.95))
