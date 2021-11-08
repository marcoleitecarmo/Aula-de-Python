from pessoa import Pessoa

p1 = Pessoa('Luiz', 35)
p2 = Pessoa('João', 23)

p1.comer('maçã')
p1.falar('POO')
p1.para_comer()
p1.falar('POO')
p1.comer('pizza')
p1.para_falar()
p1.falar('Rock Roll')

p1.falar('Filmes')
p2.comer('churrasco')

print()
print('*' * 50)

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)

print()
print('*' * 50)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print('*' * 50)

p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()



