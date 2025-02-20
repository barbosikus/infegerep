a = open('26_2653.txt')
n = int(a.readline())
f = [int(q) for q in a]
arr = set()

for i in f:
    sarr = arr.copy()
    arr.add(i)
    for j in sarr:
        arr.add(i+j)
