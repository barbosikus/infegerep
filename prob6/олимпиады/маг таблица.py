m = int(input())
n = int(input())
k = int(input())
p = (n-1)*m
if n<k:
    p+=(m-1)*n
print(p)