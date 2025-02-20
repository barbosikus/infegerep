"""
На вход программы поступает последовательность
из N целых положительных чисел.
Рассматриваются все четвёрки различных элементов последовательности.

Необходимо определить максимальную сумму четвёрки чисел,
произведение которых кратно 12.

Входные данные.

Даны два входных файла (файл A и файл B),
каждый из которых содержит в первой строке количество чисел
N (2 ≤ N ≤ 10000).
В каждой из последующих N строк записано одно целое положительное число,
не превышающее 100 000.

Программа должна вывести в первой строке одно число:
максимальную сумму четвёрки чисел, произведение которых кратно 12.

Пример организации исходных данных во входном файле:
10
30
6
23
13
39
21
85
3
17
59

Для указанных входных данных значением искомой суммы должно быть число 180.

В ответе укажите два числа:
сначала значение искомой суммы для файла А,
затем для файла B.

Предупреждение: для обработки файла B не следует использовать
переборный алгоритм, вычисляющий сумму для всех возможных вариантов,
поскольку написанная по такому алгоритму программа
будет выполняться слишком долго.
"""
f = [int(q) for q in open('B14.txt')]
n = [[] for i in range(6)]
for i in f:
    if i%12 == 0:
        n[0].append(i)
    elif i %6==0:
        n[1].append(i)
    elif i %4==0:
        n[2].append(i)
    elif i %3==0:
        n[3].append(i)
    elif i%2==0:
        n[4].append(i)
    else:
        n[5].append(i)
g = []
for i in range(len(n)):
    n[i]=sorted(n[i])
def mx(x):
    k = 0
    ki = 0
    for i in range(len(x)):
        m = x[i][-1]
        if m>k:
            k = m
            ki = i
    return (k, ki)

ncopy = [i for i in n]


t = [n[0][-1]]
del n[0][-1]
k, ki = mx(n)
t.append(k)
del n[ki][-1]
k, ki = mx(n)
t.append(k)
del n[ki][-1]
k, ki = mx(n)
t.append(k)
del n[ki][-1]
g.append(sum(t))
n =[i for i in ncopy]

t = [n[1][-1]]
kim = []
del n[1][-1]
k, ki = mx(n)
t.append(k)
kim.append(ki)
del n[ki][-1]
k, ki = mx(n)
t.append(k)
kim.append(ki)
del n[ki][-1]
if kim[0] in [0,1,2,4] or kim[1] in [0,1,2,4]:
    k, ki = mx(n)
    t.append(k)
    del n[ki][-1]
else:
    k, ki = mx([n[0], n[1], n[2], n[4]])
    t.append(k)
    del n[ki][-1]
g.append(sum(t))

n =[i for i in ncopy]
t = [n[2][-1]]
kim = []
del n[2][-1]
k, ki = mx(n)
t.append(k)
kim.append(ki)
del n[ki][-1]
k, ki = mx(n)
t.append(k)
kim.append(ki)
del n[ki][-1]
if kim[0] in [0,1,3] or kim[1] in [0,1,3]:
    k, ki = mx(n)
    t.append(k)
    del n[ki][-1]
else:
    k, ki = mx([n[0], n[1], n[3]])
    t.append(k)
    del n[ki][-1]
g.append(sum(t))

n =[i for i in ncopy]
t = [n[3][-1]]
kim = []
del n[3][-1]
k, ki = mx(n)
t.append(k)
kim.append(ki)
del n[ki][-1]
k, ki = mx(n)
t.append(k)
kim.append(ki)
del n[ki][-1]
if kim[0] in [0,2] or kim[1] in [0,2] or kim == [4,4]:
    k, ki = mx(n)
    t.append(k)
    del n[ki][-1]
else:
    if kim[0]==4 or kim[1]==4:
        k, ki = mx([n[0], n[2], n[4]])
    else:
        k,ki = mx([n[0], n[2]])
    t.append(k)
    del n[ki][-1]
g.append(sum(t))

n =[i for i in ncopy]
t = [n[4][-1]]
kim = []
del n[4][-1]
k, ki = mx(n)
t.append(k)
kim.append(ki)
del n[ki][-1]
k, ki = mx(n)
t.append(k)
kim.append(ki)
del n[ki][-1]
if kim[0] in [0,1] or kim[1] in [0,1] or kim == [3,4] or kim == [4,3]:
    k, ki = mx(n)
    t.append(k)
    del n[ki][-1]
else:
    if kim[0]==4 or kim[1]==4:
        k, ki = mx([n[0], n[1], n[3]])
    elif kim[0]==3 or kim[1]==3:
        k, ki = mx([n[0], n[1], n[4]])
    else:
        k,ki = mx([n[0], n[1]])
    t.append(k)
    del n[ki][-1]
g.append(sum(t))
print(max(g))