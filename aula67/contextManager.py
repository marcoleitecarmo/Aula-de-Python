class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        # Não tratei a exceção
        return True


# arquivo = open('abc.txt', 'w')
# arquivo.write('Alguma coisa')
# arquivo.close()

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Novo Arquivo')
