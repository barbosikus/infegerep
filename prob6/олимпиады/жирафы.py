n = int(input())
podushka = 1
a = []
while podushka<=n:
    n -=podushka
    a.append(podushka)
    podushka*=2
a.append(n)
print(a)