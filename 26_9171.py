a = open('26_9171.txt')
m,k,n = map(int, a.readline().split())
f = [list(map(int, i.split())) for i in a]
#while True:
#    i = 0
#    while i<(len(f)-1):
#        if f[i][0]>f[i+1][0] or (f[i][0]==f[i+1][0] and f[i][1]<f[i+1][1]):
#            m = f[i]
#            f[i]=f[i+1]
#            f[i+1] = m
#            break
#        i+=1
#
#    if i==(len(f)-1):
#        break

def quick_sort(x):
    if len(x)<=1:
        return x
    else:
        pivot = x[0]
        l = [i for i in x[1:] if i[0]<pivot[0] or (i[0]==pivot[0] and i[1]>pivot[1])]
        r = [i for i in x[1:] if i[0]>pivot[0] or (i[0]==pivot[0] and i[1]<=pivot[1])]
        return quick_sort(l) + [pivot] + quick_sort(r)
f = quick_sort(f)
print(f)
coun = 0
h = 0
c = [0 for i in range(k)]
for i in range(m):
    fl = 1
    for l in range(len(c)):
        if c[l] == 0:
            fl = 0
        elif c[l] == i:
            c[l] = 0
            coun+=1
    h+=fl

    for j in f:
        if i == j[0]:
            for l in range(len(c)):
                if c[l] == 0:
                    c[l] = j[1]
                    break
        elif i<j[0]:
            break


print(coun,h)