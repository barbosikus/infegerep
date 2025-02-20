f = open('27_B_17916.txt')
f.readline()
q = [list(map(float, i.replace(',', '.').split())) for i in f]
cl = [[],[],[],[],[]]
for i in range(len(q)):
    if q[i][1]>q[i][0]+4:
        cl[0].append(q[i])
    elif q[i][1]<5:
        cl[1].append(q[i])
    elif q[i][1]<9:
        cl[2].append(q[i])
    elif q[i][1]<13:
        cl[3].append(q[i])
    else:
        cl[4].append(q[i])
def dis(p1,p2):
    return ((p2[0] - p1[0])**2+(p2[1] - p1[1])**2)**0.5
def centr(cl):
    m = []
    for i in cl:
        sm = sum(dis(i, j) for j in cl)
        m.append([i,sm])
    return(min(m, key = lambda a: a[1])[0])
c = [centr(cl[0]), centr(cl[1]), centr(cl[2]), centr(cl[3]), centr(cl[4])]
print((c[0][0] + c[1][0]+ c[2][0]+c[3][0]+c[4][0])/5 *10000, (c[0][1] + c[1][1]+ c[2][1]+ c[3][1]+ c[4][1])/5*10000)