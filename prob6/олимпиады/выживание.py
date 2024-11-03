n = int(input())
l = [int(input()) for i in range(n*4)]
l50 = l[:len(l)//2+1]
stl = set(l)
for i in range(n):
    if l50.count(i)==4:
        continue
    lcopy = [i for i in l]
    l50copy = [i for i in l50]
    c = l50.count(i)
    k = 1
    cmax = -1
    for j in stl:
        if i!=j:
            lcopy.remove(j)
            lcopy.remove(j)
            lcopy.remove(j)
            lcopy.remove(j)
            l50copy = lcopy[:len(lcopy) // 2 + 1 - 2*k]
            k+=1
            if c>l50copy.count(i):
                print(cmax)
                break
            elif c<l50copy.count(i):
                cmax = max(cmax, l50copy.count(i)-c)
    else:
        print(cmax)


