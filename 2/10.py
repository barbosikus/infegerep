"""
Логическая функция F зависит от переменных x,y,z и задаётся
выражением ¬(x ≡ y -> z). На рисунке приведён частично заполненный
фрагмент таблицы истинности функции F, содержащий неповторяющиеся
строки. Определите, какому столбцу таблицы истинности функции F
соответствует каждая из переменных x,y,z.

?  ?  ?  F
0  0  1  1
0  1  1  0

В ответе напишите буквы x,y,z в том порядке, в котором идут
соответствующие им столбцы. Буквы в ответе пишите подряд, никаких
разделителей между буквами ставить не нужно.
"""
from itertools import  product
for x,y,z in product((0,1), repeat = 3):
        print(y,x,z,True if not(x == (y <= z)) else False)
        '''ответ yxz'''