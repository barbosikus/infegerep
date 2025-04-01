a = open('9.txt')
f = [list(map(int, i.split('\t'))) for i in a]
c = 0
for i in f:
    k = 0
    for j in i:
        if j % 2 != 0:
            k += 1
    if (len(list(set(i)))!=4) ^ (k==3):
        c+=1
print(c)