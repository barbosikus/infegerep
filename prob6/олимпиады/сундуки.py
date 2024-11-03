dict = {
    'A': 500,
    'B': 1000,
    'C': 5000,
    'D': 10_000,
    'E': 20_000,
    'F': 50_000,
    'G': 100_000,
    'H': 200_000,
    'I': 500_000,

    'a': 1,
    'b': 5,
    'c': 10,
    'd': 50,
    'e': 100,
    'f': 200,
    'g': 500,
    'h': 1000,
    'i': 2500
}
n = int(input())


def f(x):
    i = 0
    res = 0
    sum = ''
    while i < len(x):
        if 48 <= ord(x[i]) <= 57:
            sum += x[i]
        else:
            res += int(sum)*dict[x[i]]
            sum = ''
        i += 1
    return res


arr = [f(input()) for i in range(n)]
mx = 0
mn = float('inf')
mni = 0
mxi = 0
for j in range(len(arr)-1, -1, -1):
    if mx < arr[j]:
        mx = arr[j]
        mxi = len(arr)-j
    if mn > arr[j]:
        mn = arr[j]
        mni = len(arr)-j
print(mni, mxi, arr)