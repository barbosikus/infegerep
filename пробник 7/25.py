from itertools import *
c = []

for x,y,z,w in product(range(10), repeat = 4):
    k = int(f'3{x}12{y}14{z}{w}5')
    if k%1917 == 0:
        c.append(k)
for x,y in product(range(10), repeat = 2):
    k = int(f'3{x}12{y}14{z}5')
    if k%1917 == 0:
        c.append(k)
for x,y in product(range(10), repeat = 2):
    k = int(f'3{x}12{y}145')
    if k%1917 == 0:
        c.append(k)
c = sorted(c)[::-1]
for i in c:
    print(i, i//1917)
