n = int(input())
a = int(input())
b = int(input())
arr = [int(input()) for i in range(n)]
dict = {}
def f(x):
    res = ''
    xcopy = x
    while x > 0:
        if x%b == 0 and x//b<(x-a):
            x//=b
            res = 'B'+res
        else:
            x-=a
            res = 'A'+res
        if dict.get(x)!= None:
            if dict[x]!= '0':
                res = dict[x] + res
                dict[xcopy] = res
                return res
            else:
                dict[xcopy] = '0'
                return '0'
    if x != 0:
        res = '0'
    dict[xcopy] = res
    return res
for i in arr:
    print(f(i))