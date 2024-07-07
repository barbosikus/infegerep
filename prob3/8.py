"""
Сколько существует семизначных семеричных чисел, которые содержат в своей
записи ровно две чётные цифры?
"""
from itertools import *
c = 0
for s in product('0123456', repeat = 7):
    s = ''.join(s)
    s = s.replace('2','6').replace('4','6')
    if s[0]!='0' and (s.count('6')+s.count('0'))==2:
        c+=1
print(c)
