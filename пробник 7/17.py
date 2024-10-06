f = [int(q) for q in open('17.txt')]
mn = min(f)
print(mn)
c = 0
a = []
for x,y in zip(f, f[1:]):
    if x%16 == mn or y%16 == mn:
        c+=1
        a.append(x+y)
print(c, max(a))