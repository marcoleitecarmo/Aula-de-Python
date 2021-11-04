import cnpj

for i in range(10):
    novo_cnpj = cnpj.gera()
    formatado = cnpj.formata(novo_cnpj)
    print(formatado)
