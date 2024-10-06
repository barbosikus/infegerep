def f(a,c,m):
    if a<=19:
        return c%2==m%2
    if c==m:
        return 0
    h = [f(a-2, c+1,m),f(a-5,c+1,m),f(a//3,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
for s in range(20, 200):
    for m in range(1,5):
        if f(s,0,m):
            print(s,m)
            break
