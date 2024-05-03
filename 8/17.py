"""
Ксюша составляет слова, меняя местами буквы в слове МИМИКРИЯ.
Сколько различных слов, включая исходное, может составить Ксюша?
"""
from  itertools import *
c = 0
a = []
for z in permutations('mimikria'):
    s = ''.join(z)
    if s not in a:
        a.append(s)
        c+=1
print(c)