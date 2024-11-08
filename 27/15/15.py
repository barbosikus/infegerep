"""
Дана последовательность N целых неповторяющихся положительных чисел.
Рассматриваются все пары элементов последовательности,
разность которых делится на m = 80

Среди всех таких пар нужно найти и вывести максимальную разность элементов.

Описание входных и выходных данных

Даны два входных файла (файл A и файл B),
каждый из которых содержит в первой строке входных данных количество чисел
N (2 ≤ N ≤ 10 000).
В каждой из последующих N строк записано одно натуральное число,
не превышающее 100 000.

Пример входных данных:
8
95
163
5
40
15
3
85
80

Пример выходных данных для приведённого выше примера входных данных: 160

Предупреждение: для обработки файла B не следует использовать
переборный алгоритм, вычисляющий сумму для всех возможных вариантов,
поскольку написанная по такому алгоритму программа
будет выполняться слишком долго.
"""
