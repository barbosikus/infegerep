"""
Аня составляет трёхзначные числа в десятичной системе счисления,
в которых цифры расположены в порядке неубывания. Сколько
различных чисел может составить Аня?
"""
from  itertools import *
c =0
for z in product('123456789',repeat = 3):
    s = ''.join(z)
    if s[0]<=s[1] and s[1]<=s[2]:
        c+=1
print(c)