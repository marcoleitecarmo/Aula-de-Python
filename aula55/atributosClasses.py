
class A:
    vc = 123


a1 = A()
a2 = A()

A.vc = 15*15

print(a1.vc)
print(a2.vc)
print(A.vc)
