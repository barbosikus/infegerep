n = int(input())
m = int(input())
l = [int(input()) for i in range(n)]
r = [int(input()) for i in range(m)]
i, j = 0, 0
while i<n:
    for j in range(len(r)):
        if l[i]<=r[j] and l[i]%2 == r[j]%2:
            print((r[j]-l[i])//2, (l[i]+r[j])//2)
            r.pop(j)
            break
    else:
        print(0, l[i])
    i+=1
for j in range(len(r)):
    print(0, r[j])