"""
Логическая функция F задаётся выражением (a ∧ ¬c) ∨ (¬b ∧ ¬c).
Определите, какому столбцу таблицы истинности функции F
соответствует каждая из переменных a,b,c.

?	?	?	F
0	0	0	1
0	0	1	0
0	1	0	0
0	1	1	0
1	0	0	1
1	0	1	0
1	1	0	1
1	1	1	0

В ответе напишите буквы a,b,c в том порядке, в котором
идут соответствующие им столбцы.
"""
from itertools import product
for a,b,c in product((0,1), repeat = 3):
    if (a and not c) or (not b and not c):
        print(a, b, c)
'abc'