f = [int(q) for q in open('17 (1).txt')]
c = 0
g = []
for i in f:
    if i%2042==0:
        c+=1
for x,y in zip(f, f[1:]):
    if (x+y)>c:
        g.append(x+y)
print(len(g), max(g))