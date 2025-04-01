from itertools import *
c = 0
for z in product('01', repeat = 19):
    s = ''.join(z)
    if (s.count('1')+5)%3==0:
        c+=1
print(c)