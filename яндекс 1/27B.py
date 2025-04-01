f = [list(map(float, i.split())) for i in open('27_B.txt')]
c = []
k = 0
s = 0
def dist(p1,p2):
    return ((p2[0] - p1[0])**2+(p2[1] - p1[1])**2)**0.5

def ani(x):
    global f,s,k
    if 3<=x[1]<=4 and 2<=x[0]<=4 or 2<=x[1]<=3 and 3<=x[0]<=4:
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