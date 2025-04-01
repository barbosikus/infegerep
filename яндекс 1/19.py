def f(a,b,c,m):
    if (a+b)>=181:
        return c%2==m%2
    if c == m:
        return 0
    h = [f(a+4,b,c+1,m),f(a,b+4,c+1,m),f(a*3,b,c+1,m),f(a,b*3,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for s in range(1,156):
    for m in range(1, 5):
        if f(25,s,0,m):
            print(s,m)
            break