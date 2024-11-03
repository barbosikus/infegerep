n = int(input())
a = int(input())
l = 2*(n-a)
while n>0:
    l = l + (n-a)+(n-2*a)
    n = n - a
print(l+a)