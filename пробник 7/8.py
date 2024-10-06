from itertools import *
c = 0
for z in product('0123456789ab', repeat = 5):
    s = ''.join(z)
    if s[0]!='0'and s.count('7') == 1:
        s.replace('9', '*').replace('a', '*').replace('b', '*')
        if s.count('*')<=3:
            c+=1
print(c)