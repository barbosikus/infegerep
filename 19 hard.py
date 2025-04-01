def f(a,b,c,m):
    if a+b>=107:
        if c%2==m%2:
            print(a+b)
        return c%2==m%2
    if c == m:
        return 0
    h = [f(a+10,b,c+1,m), f(a,b+10,c+1,m),f(a*2,b,c+1,m),f(a,b*2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else any(h)
for s in range(1,101):
    for m in range(5):
        if f(5,s,0,m):
            print(s,m)
            break