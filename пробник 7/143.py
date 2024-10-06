def f(x):
    b = ''
    while x>0:
        b+=str(x%7)
        x//=7
    b = b[::-1]
    return(b)
for x in range(1, 2031):
    n = 7**170+7**100-x
    b = f(n)
    if b.count('0') == 71:
        print(x)