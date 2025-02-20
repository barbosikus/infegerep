k, n = map(int, input().split())
arr = [{} for i in range (k+1)]
for i in range(n):
    l,r,t,v = map(int, input().split())
    for j in range(l,r+1):
        arr[j][t] = v

def f(x, y):
    s = []
    for i in range(len(x)):
        if x[i]>y:
            break
        s.append(x[i])
    return s
m = int(input())
for i in range(m):
    l,r,t = map(int, input().split())
    v = 0
    for j in range(l, r+1):
        key = f(sorted(list(arr[j].keys())), t)
        for k in key:
            v+= arr[j][k]
    print(v)
