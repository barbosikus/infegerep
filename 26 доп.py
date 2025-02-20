f = open('26_17537.txt')
n, m, k = map(int,f.readline().split())
arr = [m for i in range(k)]
for i in range(n):
    y, x = map(int,f.readline().split())
    if arr[x-1]>y:
        arr[x-1] = y
mx = 0
q = 0

for i in range(k-1):
    t = min(arr[i], arr[i+1])
    if mx <= t:
        mx = t-1
        q = i+2

print(mx, q)