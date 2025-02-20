a = []
for i in open('5A.txt'):
    try:
        a.append(list(map(float, i.replace(',','.').split())))
    except ValueError as c:
        print(c, a)
f = a
cl = [[],[]]
for i in f:
    if i[0]<=6 and i[1]< -2*i[0]+16 and i[1]>4*i[0]-20:
        cl[0].append(i)
    else:
        cl[1].append(i)
def dist(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
def cen(cl):
    g = []
    for i in cl:
        s = sum(dist(i,j) for j in cl)
        g.append([s,i])
    return min(g, key = lambda a: a[0])[1]
c1 = cen(cl[0])
c2 = cen(cl[1])
x = (c1[0]+c2[0])/2*100000
y = (c1[1]+c2[1])/2*100000
print(x,y)