for i in range(1000, 10000):
    c = [g for g in range(1, int(i**0.5)+1) if i%g==0]
    c += [i//j for j in c]
    s = sum(list(set(c)))
    if str(s)[-2:] == '23':
        print(i, s)