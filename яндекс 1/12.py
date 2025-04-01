def f(x):
    while '002' in x or '22' in x:
        if '002' in x:
            x = x.replace('002', '44', 1)
        else:
            x = x.replace('22', '0', 1)
        if '222' in x:
            x = x.replace('222', '2', 1)
    return x
for n in range(3, 10001):
    s = sum(map(int,f('0' + '2'*n)))
    if s == 42:
        print(n)
