"""
Операнды арифметического выражения записаны в системе счисления с
основанием 15.

123х5₁₅ + 1х233₁₅

x * 15 + x * 15^3

В записи чисел переменной x обозначена неизвестная цифра из
алфавита 15-ричной системы счисления. Определите наименьшее
значение x, при котором значение данного арифметического
выражения кратно 14. Для найденного значения x вычислите частное
от деления значения арифметического выражения на 14 и укажите его
в ответе в десятичной системе счисления. Основание системы счисления
в ответе указывать не нужно.
"""
for x in range(0, 16):
    if (int('12305', 15) + int('10233', 15) + x * 15 + x * (15 ** 3)) % 14 == 0:
        print((int('12305', 15) + int('10233', 15) + x * 15 + x * 15 ** 3)//14)
        break