c = []
for n in range(1, 100):
    b = bin(n)[2:]
    b = b[:-2]+'10' if n%2!=0 else '10' + b[2:] +'1'
    r = int(b,2)
    if n>=26:
        c.append(r)
print(min(c))
