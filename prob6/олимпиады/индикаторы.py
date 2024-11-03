n = int(input())
nums = []
nd = [
    [1,2,3,4,5,6],
    [2,3,8],
    [1,2,4,7],
    [1,7,8,9],
    [2,3,6,9],
    [1,3,4,6,9],
    [3,4,5,8,9],
    [1,5,8],
    [1,2,3,4,5,6,9],
    [1,2,6,7,9]
]
b = []
for i in range(n):
    nums.append(int(input()))
    b.extend(nd[nums[-1]])
b = list(set(b))
for i in range(len(nd)):
    for j in range(len(nd[i])):
        if nd[i][j] not in b:
            break
    else:
        print(i)