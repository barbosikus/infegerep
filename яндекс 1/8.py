from itertools import *
c = 0
for z in product('biknopr', repeat = 6):
    s = ''.join(z)
    c+=1
    if s.count('o')==3 and len(list(set(s))) == 4:
        print(s,c)