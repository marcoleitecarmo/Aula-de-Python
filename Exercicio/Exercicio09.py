string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
comp = [letra for letra in string]
n = 10
contadores = [i for i in range(0, len(string), n)]
tuplas = [(i, i + n) for i in range(0, len(string), n)]
lista = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)

print(comp)
print(contadores)
print(tuplas)
print(lista)
print(retorno)
