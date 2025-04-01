a = open('24.txt').readline()
ch = ['1','2','3','4','5','6','7','8','9']
zn = ['+', '*']
def f(x, i, s):
    z = ''
    if len(x) == i:
        return z
    if s == 0:
        if x[i] in ch:
            z = x[i] + f(x,i+1, 1)
        if x[i] == '0':
            z = x[i] +f(x, i+1, 3)
    if s == 1 or s == 2:
        if x[i] in ch or x[i] == '0':
            z = x[i] +f(x, i+1, 2)
        if x[i] in zn:
            z = x[i] +f(x, i+1, 0)
    if s == 3:
        if x[i] in zn:
            z = x[i] +f(x, i+1, 0)
    return z
j = 0
arr = []
while (len(a)-j)>0:
    h = f(a, j, 0)
    if len(h)!=0 and h[-1] in zn:
        h = h[:-1]
    arr.append(h)
    j += len(h)+1
def g(arr):
    return max(arr, key = lambda a: len(a) if k(a) else 0)
def p(x):
    a = x[0]
    for i in range(1, len(x)):
        a*= x[i]
    return a

def k(x):
    if x == '':
        return False
    y = x.split('+')
    y = sum([p(list(map(int, a.split('*')))) for a in y])
    if len(x) == 169:
        print(y)
    return y == 0

print(g(arr))












