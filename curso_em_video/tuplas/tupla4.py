import random
n = random.randint(0,1000)
m = random.randint(0,1000)
x = random.randint(0,1000)
y = random.randint(0,1000)
z = random.randint(0,1000)

tupla = [n, m, x, y, z]

print(tupla)
print(f'Maior elemento:{max(tupla)}')
print(f'Menor elemento:{min(tupla)}')