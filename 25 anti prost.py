arr = {}
a = 1
for i in range(1,10**6):
    a*=i
    if a>=10**11:
        a//=i
        break
print(a, 13)
for j in range(14,23):
    a//=(j-1)
    a*=j
    if a>10**11:
        a//=j
        break
    print(a,13)
a//=12
a*=(10**6+1)
for j in range(10**6,12,-1):
    a*=j
    a//=j+1
    if a<10**11:
        print(a, 12)