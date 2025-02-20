n = int(input())
a = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))
for i in range(q):
    b = {}
    for j in a:
        if b.get(j//x[i]):
            b[j//x[i]] +=1
        else:
            b[j // x[i]] = 1
    max = 0
    for i in b.keys():
        if b[i] > max:
            max = b[i]
    print(max)
