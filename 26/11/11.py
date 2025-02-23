"""
Организация купила для своих сотрудников все места в нескольких
подряд идущих рядах на концертной площадке. Известно, какие места
уже распределены между сотрудниками. Найдите ряд с наибольшим номером,
в котором есть два соседних места, таких что слева и справа от них
в том же ряду места уже распределены (заняты). Гарантируется, что
есть хотя бы один ряд, удовлетворяющий условию. В ответе запишите
два целых числа: номер ряда и наименьший номер места из найденных
в этом ряду подходящих пар.

Входные данные. В первой строке входного файла находится одно
число: N – количество занятых мест (натуральное число, не
превышающее 10 000). В следующих N строках находятся пары чисел:
ряд и место выкупленного билета (числа не превышают 100 000).

Выходные данные. Два целых неотрицательных числа:
Максимальный номер ряда, где нашлись обозначенные в задаче места
и минимальный номер места.

Пример входного файла:
6
50 12
50 15
60 157
60 160
60 22
60 25

Выходные данные: 60 23
"""
