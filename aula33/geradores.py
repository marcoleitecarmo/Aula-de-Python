import sys
import time

lista = list(range(10))

print(sys.getsizeof(lista))
print(lista)

print("=" * 100)


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()
for v in g:
    print(v, end=' ')
print()

print(hasattr(g, '__next__'))
print(hasattr(g, '__iter__'))

print('%' * 100)

l1 = [x for x in range(1000)]
print(type(l1))
l2 = (x for x in range(1000))
print(type(l2))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
