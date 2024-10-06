def f(x):
    while '11111' in x or '888' in x:
        if '11111' in x:
            x = x.replace('11111', '88', 1)
        else:
            x = x.replace('888', '8', 1)
    return x
print(f('1'*81))