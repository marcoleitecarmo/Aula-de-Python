lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

listasoma = []
for i in range(len(lista2)):
    listasoma.append(lista1[i] + lista2[i])
print(listasoma)

print('@' * 100)

listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]

listaS = [x + y for x, y in zip(listaA, listaB)]
print(listaS)
