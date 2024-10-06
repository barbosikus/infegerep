from itertools import *
def f(x):
    b = ''
    while x>0:
        b+=str(x%19)
        x//=19
    b = b[::-1]
    return(b)
for x in product('0123456789abcdefghi', repeat = 1):
    i = ''.join(x)
    n = int(f'98897{i}21', 19) + int(f'2{i}923', 19)
    if n%18 == 0:
        print(i, n//18)
