import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
v = copy.deepcopy(d1)

v[1] = 'Luiz'
v['d'][0] = 'Joãozinho'

print(d1)
print(v)
