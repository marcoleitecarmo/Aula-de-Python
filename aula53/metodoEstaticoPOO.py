from pessoa import Pessoa

p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print('*' * 50)
print(Pessoa.gera_id())
print(p1.gera_id())
