t = int(input())
a,b,c = sorted(map(int, input().split()))[::-1]
k = 0
if (a-c)%2 == 0:
    d = c + (a - c)//2
    mx = max(b, d)
    mn = min(b,d)
    if (mx - mn)%3 == 0:
        print('yes')
        if abs(a - b) > abs(c - b):
            k+=(b - c)
            mx = a - (b - c)
            mn = b
            k+= ((mx - mn)//3) * 2
            print(k)
        if abs(a - b) < abs(c - b):
            k += (a - b) * 2
            mn = c + (a - b)
            mx = b
            k += ((mx - mn) // 3) * 2
            print(k)
else:
    print('no')



