l1 = list(range(100))
ex1 = [v for v in l1 if v % 2 == 0]
ex2 = [v for v in l1 if v % 3 == 0]
ex3 = [v for v in l1 if v % 5 == 0 if v % 8 == 0]
ex4 = [v if v % 3 == 0 else 0 for v in l1]
ex5 = [v if v % 3 == 0 and v % 8 == 0 else '*' for v in l1]
ex6 = [v if v % 3 == 0 or v % 5 == 0 else '#' for v in l1]

print(l1)
print(ex1)
print(ex2)
print(ex3)
print(ex4)
print(ex5)
print(ex6)
