a = open('26_18228.txt')
n, r = map(int, a.readline().split())
f = [list(map(int, i.split())) for i in a]
for i in range(n):
    f[i] = sorted(f[i])[::-1]
s = 0
c = []
fd = {i:j for i,j in zip(range(1,n+1), f)}
print(fd[2898])
fdcopy = sorted(fd.items(), key = lambda a: a[1][0])[::-1]
i = 0
d = 0
while s<2*r:
    s+=fdcopy[i][1][0]
    c.append(fdcopy[i][0])
    i+=1
    d = fdcopy[i][1][0]
    #print(d)
c.pop(-1)
fdcopy = sorted(fd.items(), key = lambda a: a[1][-1])
posl = d -(s - 2*r)
print(posl)
k = []
for j in range(len(max(fdcopy, key = lambda a: len(a[1]))[1])):
    for i in fdcopy:
        if len(i[1])>j and i[1][-j-1]>=posl:
            k.append([i[0], i[1][-j-1]])
            break
print(len(c)+1, min(k, key = lambda a: a[1])[0])
