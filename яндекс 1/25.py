for x in range(700_000, 1_000_000):
    g = [j for j in range(1,int(x**0.5)+1) if x%j == 0]
    g += [x//j for j in g]
    g = sorted(g)
    for i in g:
        i = str(i)
        if i[-1] == '7' and i!='7' and i!=x:
            print(x, i)
            break