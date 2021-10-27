from vendas.formata import fpreco


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    if formata:
        return fpreco.real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))
    if formata:
        return fpreco.real(r)
    else:
        return r
