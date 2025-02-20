x,y,k,l = map(int, input().split())
l = 2*l
def f(start, end):
    if end<x or start>y:
        return 0
    if end>y:
        end = y
    if start<x:
        start = x
    s = 0
    if (end - start)%l==0:
        s+=(end - start)//l
    else:
        s += (end - start) // l + 1
    return s
sk = 0
for i in range((x-k)-abs(x-k)%k, (y+k)+(k-abs(y+k)%k), k):
    sk+=f(i+l/2, i+k-l/2)
    print(sk, i)
print(sk)