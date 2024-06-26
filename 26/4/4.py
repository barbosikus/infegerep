"""
На грузовом судне необходимо перевезти контейнеры, имеющие одинаковый
габарит и разные массы. Общая масса всех контейнеров превышает
грузоподъёмность судна. Количество грузовых мест на судне не меньше
количества контейнеров, назначенных к перевозке. Определите минимальное
количество контейнеров, которое может остаться после погрузки, и их
наибольшую возможную суммарную массу.

Входные данные.

В первой строке входного файла находятся два числа:
S – грузоподъёмность судна (натуральное число, не превышающее 100 000)
и N – количество контейнеров (натуральное число, не превышающее 10 000).
В следующих N строках находятся значения масс контейнеров, требующих
транспортировки (все числа натуральные, не превышающие 100), каждое
в отдельной строке.

Выходные данные.

Два целых неотрицательных числа: минимальное количество контейнеров,
которое может остаться после погрузки, и их наибольшая возможная
суммарная масса.

Пример входного файла:

100 5
80
30
50
40
20

При таких исходных данных можно транспортировать за один раз максимум
три контейнера. Возможные объёмы этих трёх контейнеров:
30, 50, 20; 30, 40, 20;. Для приведённого примера минимальное
количество контейнеров, которые останутся, равно 2, их максимально
возможная суммарная масса составляет 130.
"""
