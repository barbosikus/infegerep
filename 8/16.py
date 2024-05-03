"""
Вика составляет четырёхбуквенные слова из букв А, Й, У, В, Ф
причём слово не может начинаться с буквы Й и не должно содержать
сочетаний ВФ и ФВ. Все буквы в слове различны. Сколько таких слов
может составить Вика?
"""
from itertools import *
c = 0
for z in product('ayuvf', repeat = 4):
    s = ''.join(z)
    if s.count('a')<=1 and s.count('y')<=1 and s.count('u')<=1 and s.count('v')<=1 and s.count('f')<=1:
        if s[0]!='y' and 'vf' not in s and 'fv' not in s:
            c+=1
print(c)