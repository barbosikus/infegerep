"""
Миша заполнял таблицу истинности функции
(x ∨ ¬y) ∧ ¬(y ≡ z) ∧ w, но успел заполнить лишь фрагмент
из трёх различных её строк, даже не указав, какому столбцу
таблицы соответствует каждая из переменных.

?   ?   ?   ?   F
0	1	 	0	1
 	1	1	0	1
1	 	0	 	1

Определите, какому столбцу таблицы соответствует каждая из переменных
w, x, y, z. В ответе напишите буквы w, x, y, z в том порядке, в котором
идут соответствующие им столбцы (сначала буква, соответствующая
первому столбцу; затем буква, соответствующая второму столбцу, и т.д.).
Буквы в ответе пишите подряд, никаких разделителей между буквами
ставить не нужно.
"""



for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (x or not y) and not(y == z) and w:
                    print(x, w, z, y)
