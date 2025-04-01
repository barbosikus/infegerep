import sys
sys.setrecursionlimit(100000)

class les:
    def __init__(self, id, cnt, dep, arr):
        self.id = id
        self.cnt = cnt
        self.dep = [i for i in arr if i.id in dep]
        self.start = 0
        self.recreate()
    def next(self):
        return self.cnt + self.start + 1
    def recreate(self):
        for i in self.dep:
            self.start = max(self.start, i.next())

    def change(self, start):
        for i in self.dep:
            if i.next()<start:
                return 0
        self.start = start
        return 1
    def grab(self, mxt):
        start = 0
        for i in self.dep:
                start = max(start, i.next())
        return range(start, mxt)
a = open('221')
f = [list(map(int,i.split('\t')[:2])) + [list(map(int,i.split('\t')[2].replace('"', '').replace('\n', '').split('; ')))] for i in a]
arr = []
for i in f:
    arr.append(les(*i, arr))
mxt = max(i.next() - 1 for i in arr)
def vrema(arr, v):
    q = 0
    for t in range(mxt+1):
        c = 0
        for i in arr:
            if i.start<= t < i.next()-1:
                c+=1
        if c == v:
            q+=1
    return q
#def fd(x, v):
#    c = 0
#    mx = 0
#    for i in x:
#        if i == v:
#            c+=1
#        else:
#            c = 0
#        mx = max(mx, c)
#    return mx
def f(x):
    y = x.grab(mxt)
    mx = 0
    for i in y:
        x.change(i)
        for j in arr:
            if j.id>x.id:
                f(j)
                mx = max(mx,vrema(arr, 5))
    return mx
print(f(arr[0]))