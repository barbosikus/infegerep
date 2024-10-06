c = []
for n in range(1, 13):
    b = bin(n)[2:]
    if n%2 == 0:
        b = '10' +b
    else:
        b = '1' + b + '01'
    res = int(b,2)
    c.append(res)
print(max(c))