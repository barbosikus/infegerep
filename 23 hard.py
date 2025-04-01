def de(x):
    g = [i for i in range(1,int(x**0.5)+1) if x%i==0]
    g += [x//i for i in g if i!=x**0.5]
    return sum(g)
def f(x):
    if x==24:
        return 1
    if x>24:
        return 0
    else:
        return f(x+1)+f(de(x))
print(f(2))