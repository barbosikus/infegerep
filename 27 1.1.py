f = open('27B_18051.txt')
f.readline()
q = [list(map(float, i.replace(',', '.').split())) for i in f]
cl = []
def dis(p1,p2):
    return ((p2[0] - p1[0])**2+(p2[1] - p1[1])**2)**0.5
def centr(cl):
    m = []
    for i in cl:
        sm = sum(dis(i, j) for j in cl)
        m.append([i,sm])
    return(min(m, key = lambda a: a[1])[0])
def f(p):
    g = [p1 for p1 in q if dis(p1,p)<0.4]
    if len(g)>0:
        for p1 in g:
            q.remove(p1)
        ng = [f(p1) for p1 in g]
        g += sum(ng,[])
    return g
while len(q)>0:
    p = q.pop()
    c = [p]+f(p)
    print(len(c))
    cl.append(c)

