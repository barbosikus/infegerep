f = [list(map(float, i.split())) for i in open('27_A.txt')]
c = []
k = 0
s = 0
def dist(p1,p2):
    return ((p2[0] - p1[0])**2+(p2[1] - p1[1])**2)**0.5

def ani(x):
    global f,s,k
    if 1<=x[1]<=2 and 1<=x[0]<=3:
        h = -1
        for i in f:
            if dist(x, i)<=0.1:
                h+=1
        if h>=14:
            s+=1
        else:
            k+=1
for i in f:
    ani(i)
print(s,k)