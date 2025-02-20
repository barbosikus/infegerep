f = open('3B.txt')
a = [list(map(float, i.replace(',','.').split())) for i in f]
def dist(p1,p2):
    return max(abs(p1[0]-p2[0]), abs(p1[1]-p2[1]))
def cen(x):
    c = []
    for i in x:
        s = sum(dist(i, j) for j in x)
        c.append([s,i])
    return min(c, key= lambda a: a[0])[1]
cl = []
def f(p):
    g = [p1 for p1 in a if dist(p1, p) < 0.5]
    if len(g) > 0:
        for p1 in g:
            a.remove(p1)
        ng = [f(p1) for p1 in g]
        g += sum(ng, [])
    return g
while len(a)>0:
    p = a[0]
    a.pop(0)
    arr = [p]+f(p)
    cl.append(arr)
    print(len(a))
#cl = [[],[],[]]
#for i in a:
#    if i[0]>3:
#        cl[0].append(i)
#    elif i[1]<(-2):
#        cl[1].append(i)
#    else:
#        cl[2].append(i)
#print(len(cl[0]),len(cl[1]),len(cl[2]))
p1 = cen(cl[0])
p2 = cen(cl[1])
p3 = cen(cl[2])
x = (p1[0]+p2[0]+p3[0])/3*10000
y = (p1[1]+p2[1]+p3[1])/3*10000
print(x,y)