n = int(input())
a = list(map(int, input().split()))
for k in range(1, n+1):
    l = list(map(list, zip(*(a[i:] for i in range(k)))))
    for i in range(len(l)):
        l[i] = max(l[i])

    print(min(l), end = ' ')