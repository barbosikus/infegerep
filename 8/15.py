"""
Ада составляет шестибуквенные слова из букв Д, Е, Й, К, С, Т, Р, А.
Буква Й встречается в слове ровно один раз, и после неё обязательно
идёт согласная. Буквы в слове не повторяются. Сколько слов может
составить Ада?
"""
from itertools import *
c = 0
for z in product('deykstra', repeat = 6):
    s = ''.join(z)
    if s.count('d')<=1 and s.count('e')<=1 and s.count('y')<=1 and s.count('k')<=1 and s.count('s')<=1 and s.count('t')<=1 and s.count('r')<=1 and s.count('a')<=1:
        s = s.replace('k', 'd').replace('s', 'd').replace('t', 'd').replace('r', 'd')
        if s.count('y') == 1 and 'yd' in s :
            c+=1
print(c)