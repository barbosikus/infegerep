f = open('4B.txt')
a = [list(map(float, f.readline().replace(',','.').split())) for i in f]
def dist(p1,p2):
    return (abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))
def cen(x):
    c = []
    for i in x:
        s = sum(dist(i, j) for j in x)
        c.append([s,i])
    return min(c, key= lambda a: a[0])[1]
cl = [[],[],[]]
for i in a:
    if i[0]>20:
        cl[0].append(i)
    elif i[1]>(-2):
        cl[1].append(i)
    else:
        cl[2].append(i)
p1 = cen(cl[0])
p2 = cen(cl[1])
p3 = cen(cl[2])
x = (p1[0]+p2[0]+p3[0])/3*10000
y = (p1[1]+p2[1]+p3[1])/3*10000
print(x,y)