from itertools import *
c = 0
for z in product('01234567', repeat = 27):
    s = ''.join(z)
    if s[0]!='0':
        ch = 0
        nch = 0
        for i in '01234567':
            if s.count(i)%2==0:
                ch+=1
            else:
                nch+=1
        if nch == 1:
            c+=1
print(c%(10**9+7))