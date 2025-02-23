"""
Дана последовательность целых чисел.
Рассматриваются все её непрерывные подпоследовательности
длиной не менее семи элементов,
такие что количество положительных чисел кратных 7 делится на 7.

Найдите наибольшую сумму такой подпоследовательности.

Входные данные

Первая строка входного файла содержит целое число
N – общее количество чисел в наборе.
Каждая из следующих N строк содержит одно число.

Гарантируется, что общая сумма любой выборки заданных чисел
не превышает 2 ∙ 10⁹ по абсолютной величине.

Вам даны два входных файла (A и B),
каждый из которых имеет описанную выше структуру.
В ответе укажите два числа:
сначала значение искомой суммы для файла A,
затем для файла B.
"""
f = [int(q) for q in open('B50.txt')]
arr = [0 for i in range(7)]
q = []
c = 0
s = 0
sm = 0
for i in range(6):
    sm+=f[i]
    c+=1 if f[i]%7==0 else 0
    q.append(c)
for i in range(6, len(f)):
    sm += f[i]
    c += 1 if f[i] % 7 == 0 else 0
    if c%7==0:
        s=max(s, sm)
    s = max(s, sm - arr[c%7])
    a = q.pop(0)
    arr[a%7] = min(arr[a%7], sm)
    q.append(c)
print(s)
