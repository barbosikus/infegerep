f = [int(q) for q in open('17.txt')]
c = 0
for i in f:
    if 9<i<100:
        c+=1
k = 0
arr = []
for x,y in zip(f, f[1:]):
    x1 = str(x)[-1]
    y1 = str(y)[-1]
    s = int(x1) + int(y1)
    if s == c:
        k+=1
        arr.append(x+y)
print(k, min(arr))

