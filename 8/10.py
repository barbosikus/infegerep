"""
Сколько существует восьмеричных пятизначных чисел, не
содержащих в своей записи цифру 1, в которых все цифры
различны и никакие две чётные или две нечётные цифры не
стоят рядом?
"""
from  itertools import *
c = 0
for z in product('0234567', repeat = 5):
    s = ''.join(z)
    if s[0]!='0' and s.count('0') <= 1 and s.count('2') <= 1 and s.count('3') <= 1 and s.count('4') <= 1 and s.count('5') <= 1 and s.count('6') <= 1 and s.count('7') <= 1:
        s = s.replace('0', 'a').replace('2', 'a').replace('4', 'a').replace('6', 'a')
        s = s.replace('3', 'b').replace('5', 'b').replace('7', 'b')
        if 'aa' not in s and 'bb' not in s:
            c+=1
print(c)