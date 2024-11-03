a = []
c = 0
for i in range(2026,9001):
    for n in range(2025, i):
        a.append(n)
    a = a[::-1]
    print(a)
    while len(a)>1:
        b = a[0] - a[1]
        a = a.pop(0)
        a = a.pop(1)
        a.append(b)
        a = sorted(a)[::-1]

    if a[0] == 0:
        c+=1
print(c)