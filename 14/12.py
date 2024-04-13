"""
Определите число x, для которого выполняется равенство 103ₓ = 97ₓ₊₂.
"""
n1 = 103
n2 = 97
for x in range(2,100):
    '''for y in range(2, 100):'''
    y =x+2
    b = ''
    c = ''
    while n1>0:
        b += str(n1%x)
        n1 //=x
    b = b[::-1]
    while n2>0:
        c += str(n2%y)
        n2 //=y
    c = c[::-1]
    if b == c:
        print(x)