def impl(x, y):
    if (x == 1) and (y == 0):
        return 0
    else:
        return 1


n = int(input())
a = list(map(int, input().split()))
r = int(input())
l = impl(a[0], a[1])
for i in range(2, len(a)):
    if (l == 0) and i % 2 != 0 and r == 0:
        print(i, len(a))
        quit()
    if l == 1 and i % 2 == 0 and r == 1:
        print(i, len(a))
        quit()
    l = impl(l, a[i])
l = impl(a[-2], a[-1])
for i in range(len(a) - 3, 0, -1):
    if (l == 0) and r == 0:
        print(i, len(a))
        quit()
    if l == 1 and r == 1:
        print(i, len(a))
        quit()
    l = impl(a[i], l)
if l == r:
    print('0')
else:
    print('-1')




