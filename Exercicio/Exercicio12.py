# usando o zip_longest
from itertools import zip_longest

listaA = [1, 2, 3, 4, 50, 60, 70, 80]
listaB = [1, 2, 3, 4]

listaS = [x + y for x, y in zip_longest(listaA, listaB, fillvalue=0)]
print(listaS)
