
def f(x):
    b = ''
    while x>0:
        b+=str(x%5)
        x//=5
    b = b[::-1]
    return b
for x in range(2043):
    n = 25 ** 61 + 5 ** 178 - x
    if f(n).count('0') == 60:
        print(x)