"""
Определите количество восьмеричных пятизначных чисел,
которые не начинаются с нечётных цифр, не оканчиваются
цифрами 2 или 6, а также содержат не более двух цифр 7.
"""
from itertools import *
c = 0
for z in product('01234567',repeat = 5):
    if z[0]!='1' and z[0]!='3' and z[0]!='5' and z[0]!='7' and z[-1]!='2' and z[-1]!='6' and z.count('7')<=2 and z[0]!=0:
        c+=1
print(c)