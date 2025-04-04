"""
Дана последовательность натуральных чисел.
Известно, что сумма всех чисел последовательности не превышает 10⁹.
Рассматриваются все её непрерывные подпоследовательности,
в которых количество чисел, делящихся на 5, кратно 3.

Найдите наибольшую сумму такой подпоследовательности.

Входные данные.

Даны два входных файла,
каждый из которых содержит в первой строке количество чисел
N (2 ≤ N ≤ 100000).
Каждая из следующих N строк файлов содержит одно натуральное число,
не превышающее 10000.

Пример входного файла:
7
20
5
4
10
6
15
8

В этом наборе можно выбрать две непрерывные последовательности,
содержащие по 3 числа, делящихся на 5 (20+5+4+10+6=45)
и (5+4+10+6+15+8=48).
Ответ: 48.

В ответе укажите два числа:
сначала искомое значение для файла А,
затем для файла B.
"""
g = open('B68.txt')
f = [int(q) for q in g]
ms = [float('+inf') for i in range(3)]
s = 0
sc = 0
c = 0
for i in range(len(f)):
    sc +=f[i]
    if f[i]%5==0:
        c +=1
    if c%3==0:
        if sc > s:
            s = sc
    a = sc - ms[sc%3]
    if a>s:
        s = a
    if sc<ms[sc%3]:
        ms[sc % 3] = sc
print(s)
