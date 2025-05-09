"""
Для игры, описанной в задании 19, определите сколько существует
значений S, при которых у Пети есть выигрышная стратегия, причём
одновременно выполняются два условия:

− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того,
  как будет ходить Ваня.
"""
def f(a,c,m):
    if a>=36 and a<=60:
        return c%2==m%2
    if a>60:
        return (c+1)%2==m%2
    if c==m:
        return 0
    h = [f(a+1,c+1,m),f(a*2,c+1,m),f(a*3,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)
g = 0
for s in range(1,36):
    if f(s,0,3)==1:
        print(s)
        g+=1
print(g)