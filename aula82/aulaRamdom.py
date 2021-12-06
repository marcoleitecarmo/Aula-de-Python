import random
import string

inteiro = random.randint(10, 20)
inteiro2 = random.randrange(900, 1000, 10)
flutuante = random.uniform(10, 20)
flutuante2 = random.random()
fichas = ['Ricardo', 'Marcelo', 'Marina', 'Rita', 'Jose', 'Darcio', 'Fernando']
lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
for i in range(1000):
    sorteio = random.sample(lista, 2)

    print(sorteio)

random.shuffle(fichas)

sorteio4= random.choice(lista)
sorteio2 = random.choices(lista, k=2)
sorteio3 = random.sample(lista, 2)

print(inteiro)
print(inteiro2)
print(flutuante)
print(flutuante2)
print(sorteio4)
print(sorteio2)
print(sorteio3)
print(fichas)

