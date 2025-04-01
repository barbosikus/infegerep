f = [int(q) for q in open('17.16_14653.txt')]
m1 = float('+inf')
m2 = float('+inf')
m3 = 0
c = 0
g = []
for i in f:
    if i>0 and abs(i)%17==0 and i<=m1:
        m2 = m1
        m1 = i
for i in f:
    if abs(i)%100==69 and i>m3:
        m3=i
print(m1,m2,m3)
for x in zip(f, f[1:], f[2:], f[3:]):
    k1 = 0
    k2 = 0
    k4 = 1
    for i in x:
        if 99<abs(i)<1000:
            k1+=1
        if abs(i)%18==0:
            k2+=1
        k4*=i
    if abs(sum(x))%(m1+m2)==0 and k4<=m3**2 and k1==2 and k2 == 1:
        c+=1
        g.append(sum(x)**2)
print(c, min(g))