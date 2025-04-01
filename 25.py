for i in range(1,1000):
    n = 1_850_000_000 + i
    g = [j for j in range(1,int(n**0.5)+1) if n%j==0 and j%2==0]
    g+= [n//j for j in g if j!=n**0.5 and (n//j)%2==0]
    if len(g)%2!=0:
        print(i, len(g))

