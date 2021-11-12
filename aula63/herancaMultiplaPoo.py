class A:
    def falar(self):
        print('Falando.....em classe A')


class B(A):
    def falar(self):
        print('Falando...Classe B')


class C(A):
    def falar(self):
        print('Falando...Classe C')


class D(C, B):
    pass


d = D()
d.falar()