a = open('8B.txt')
f = [list(map(float, i.replace(',','.').split())) for i in a]
cl = []
def dist(p1,p2):
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)**0.5
def fun(p):
    arr = []
    for i in f:
        if dist(p,i)<=0.5:
            arr.append(i)
    if len(arr)>0:
        for i in arr:
            f.remove(i)
        newarr = [fun(i) for i in arr]
        arr+=sum(newarr,[])
    return arr

while len(f)>0:
    p = f.pop()
    s = fun(p)+[p]
    print(len(s))
    cl.append(s)

def cen(cl):
    g = []
    for i in cl:
        s = sum(dist(i,j) for j in cl)
        g.append([s,i])
    return min(g,key = lambda a:a[0])[1]
c =[cen(i) for i in cl]
abc = sum(x for x,y in c)/len(c)*100000
orh = sum(y for x,y in c)/len(c)*100000
print(abc,orh)