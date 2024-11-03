def f(x):
    while '33333' in x or '1111' in x:
        if '33333' in x:
            x = x.replace('33333', '111', 1)
        else:
            x = x.replace('111', '33', 1)
    return x
print(sum(list(map(int,f('3'*111)))))