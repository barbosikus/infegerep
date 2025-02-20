f = open('27B_18051.txt')
f.readline()
q = [list(map(float, i.replace(',', '.').split())) for i in f]
cl = [[],[]]
for i in range(len(q)):
    if q[i][1] > 2*q[i][0] + 4:
        cl[0].append(q[i])
    else:
        cl[1].append(q[i])
print(len(cl[0]),len(cl[1]))
def dis(p1,p2):
    return ((p2[0] - p1[0])**2+(p2[1] - p1[1])**2)**0.5
def centr(cl):
    m = []
    for i in cl:
        sm = sum(dis(i, j) for j in cl)
        m.append([i,sm])
    return(min(m, key = lambda a: a[1])[0])
c = [centr(cl[0]), centr(cl[1])]
print((c[0][0] + c[1][0])/2 *10000, (c[0][1] + c[1][1])/2*10000)

