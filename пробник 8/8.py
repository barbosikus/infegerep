from itertools import *
c = 0
for z in product('lustra', repeat = 5):
    s = ''.join(z)
    if s.count('u')<=2 and s[-1]!='l' and s[-1]!='s' and s[-1]!='t' and s[-1]!='r':
        c+=1
print(c)