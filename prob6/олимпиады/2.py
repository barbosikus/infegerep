n, q = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))
def f(i, a):
    for j in a:
        if (i - j) < 0:
            yield 0
        else:
            yield (i - j)
dict = {}
for g in a:
    # for i in range(1, 1000):
    #     if sum(f(i,a))<=g:
    #         #print(n*i - sum(a))
    #         continue
    #     else:
    #         print(i-1)
    #         break
    if g in dict:
        dict[g] +=1
    else:
        dict[g] = 1
for g in x:
    for i in range(1, 1000):
        k = 0
        c = sorted(dict)
        for j in c:
            if i - j>0:
                k+=dict[j]*(i-j)
            else:
                break
        if k<=g:
            continue
        else:
            k = i-1
            break
    print(k)