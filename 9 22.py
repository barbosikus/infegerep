a = open('9.22_20488.txt')
f = [list(map(int, i.split('\t'))) for i in a]
c = 0
for i in f:
    if 1<len(list(set(i)))<7 and i.count(max(i))==1:
        c1 = []
        c2 = []
        for j in i:
            if i.count(j)==1:
                c1.append(j)
            else:
                c2.append(j)
        if sum(c1)>=3*sum(c2):
            c+=1
print(c)