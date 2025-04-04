"""
На вход алгоритма подаётся натуральное четырёхзначное число N, в 
котором все цифры различны. Алгоритм строит по нему новое число R 
следующим образом:

- Максимальная и минимальная цифры числа складываются.
- Остальные две цифры перемножаются.
- Полученные два числа записываются друг за другом в порядке 
  неубывания (без разделителей).

Полученное число и является искомым R.

Например, для исходного числа 1234 шаги алгоритма будут такими:

1+4=5
2⋅3=6
R=56

Укажите минимальное число N, после обработки которого с помощью 
этого алгоритма получается число R, большее 85. В ответе запишите это 
число в десятичной системе счисления.
"""
from itertools import product
h = []
for a,b,c,d in product('0123456789', repeat = 4):
    if a!=b and a!=c and a!=d and b!=c and c!=d and b!=d and a!='0':
        x = str(a+b+c+d)
        h.append(x)
h = list(map(int, h))
print(h)
for n in h:
    a = n%10
    b = (n//10)%10
    c = (n//100)%10
    d = n//1000
    f = sorted(set([a,b,c,d]))
    sm = max(f) + min(f)
    prois = f[1]*f[2]
    ff = sorted([sm,prois])
    res = str(ff[0])+str(ff[1])
    if int(res) >85:
        print(n)
'''1089'''