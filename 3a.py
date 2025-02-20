f = open('3A.txt')
a = [list(map(float, f.readline().replace(',','.').split())) for i in f]
def dist(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
def cen(x):
    c = []
    for i in x:
        s = sum(dist(i, j) for j in x)
        c.append([s,i])
    return min(c, key= lambda a: a[0])[1]
cl = [[],[]]
for i in a:
    if i[1]>5:
        cl[0].append(i)
    else:
        cl[1].append(i)
p1 = cen(cl[0])
p2 = cen(cl[1])
x = (p1[0]+p2[0])/2*10000
y = (p1[1]+p2[1])/2*10000
print(x,y)
