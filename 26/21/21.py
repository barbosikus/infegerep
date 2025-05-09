"""
На кассе самообслуживания в гипермаркете за день покупатели
пробивают самые различные товары. С каждого товара касса считывает
штрихкод - это девятиразрядное натуральное число, возможно, имеющее
какое-то количество ведущих нулей. Штрихкоды различных товаров
отличаются. Маркетологу гипермаркета необходимо выяснить,
какое количество различных товаров было куплено через
кассу и какой товар покупали чаще всего.

Входные данные.

В первой строке входного файла находится число N - количество пробитых
за день штрихкодов (натуральное число, не превышающее 10 000).
В следующих N строках находятся значения штрихкодов (все числа натуральные,
меньше 109), каждое в отдельной строке.

Запишите в ответе два числа: количество различных проданных товаров и
наибольшее количество товаров с совпадающим штрихкодом.

Пример входного файла.

7
4858
112
4858
4858
31
112
4858

При таких исходных данных имеется 3 различных товара.
Наиболее часто встречающийся товар имеет штрихкод 4858.
Он встречается 4 раза. Поэтому ответ для приведённого примера: 3 4.
"""
f = open('21.txt')
a = [int(q) for q in f][1:]
print(len(set(a)))
m = 0
b = set(a)
for i in list(b):
    m = max(m, a.count(i))
print(m)