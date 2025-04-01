f = [int(q) for q in open('17_12926.txt')]
a = float('-inf')
m = max(f, key = lambda a: a if 9<abs(a)<100 else 0)
c = 0
g = []
for x in zip(f,f[1:], f[2:], f[3:]):
    k = 0
    for i in x:
        if str(i)[-1]!=str(x[0])[-1]:
            k = 1
    if k==0:
        a = max(a, sum(x))
print(m,a)
for x in zip(f,f[1:], f[2:], f[3:], f[4:]):
    k1 = 0
    for i in x:
        if i<a:
            k1+=1
    if sum(x)%m==0 and k1 == 1:
        c+=1
        g.append(sum(x))
print(c, min(g))
