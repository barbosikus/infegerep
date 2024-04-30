"""
Иван составляет 6-буквенные слова из букв A, B, C, W, X, Y, Z.
Первой и последней буквами этого слова могут быть только буквы
W, X, Y, и Z, на остальных позициях эти буквы не встречаются.
Сколько различных кодовых слов может составить Иван?
"""
print(4*3*3*3*3*4)
from itertools import *
k=0
for a,b,c,d,e,f in product("abcwxyz",repeat=6):
    if (a in "wxyz" and
        f in "wxyz" and
        b not in "wxyz" and
        c not in "wxyz" and
        d not in "wxyz" and
        e not in "wxyz"):
        k+=1
print(k)