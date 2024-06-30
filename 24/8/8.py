"""
Текстовый файл состоит из символов A, B, C, D и O.

Определите максимальное количество идущих подряд
пар символов вида согласная + гласная в прилагаемом файле.

Для выполнения этого задания следует написать программу.
"""
f = open('8.txt')
a = f.readline().replace('BA', '*').replace('CA', '*').replace('DA', '*').replace('BO', '*').replace('CO', '*')\
.replace('DO', '*').replace('A', '#').replace('B', '#').replace('C', '#').replace('D', '#').replace('O', '#').split('#')
print(len(max(a, key = len)))
