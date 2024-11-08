"""
Имеется набор данных, состоящий из троек положительных целых чисел.

Необходимо выбрать из каждой тройки два числа так,
чтобы сумма всех выбранных чисел делилась на 4
и при этом была максимально возможной.

Гарантируется, что искомую сумму получить можно.
Программа должна напечатать одно число –
максимально возможную сумму, соответствующую условиям задачи.

Входные данные: Даны два входных файла: файл A и файл B,
каждый из которых содержит в первой строке количество троек
N (1 ≤ N ≤ 100000).
Каждая из следующих N строк содержит три натуральных числа,
не превышающих 10 000.

Пример входного файла:
6
8 3 4
4 8 12
9 5 6
2 8 3
12 3 5
1 4 12

Для указанных входных данных значением искомой суммы должно быть число 88.

В ответе укажите два числа:
сначала значение искомой суммы для файла А,
затем для файла B.

Предупреждение: для обработки файла B не следует использовать
переборный алгоритм, вычисляющий сумму для всех возможных вариантов,
поскольку написанная по такому алгоритму программа
будет выполняться слишком долго.
"""