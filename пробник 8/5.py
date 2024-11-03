c = []
for n in range(1,1000):
    b = bin(n)[2:]
    if n%5==0:
        b = b[:3] + b
    if n%5!=0:
        ost = bin((n%5)*5)[2:]
        b = b+ost
    res = int(b,2)
    if res<313 and n%2!=0:
        c.append(n)
print(max(c))
