"""
Какая строка получится в результате применения приведённой
ниже программы к строке, состоящей из 70 идущих подряд цифр 8?
В ответе запишите полученную строку.

НАЧАЛО
    ПОКА нашлось (2222) ИЛИ нашлось (8888)
       ЕСЛИ нашлось (2222)
           ТО заменить (2222, 88)
           ИНАЧЕ заменить (8888, 22)
       КОНЕЦ ЕСЛИ
    КОНЕЦ ПОКА
КОНЕЦ
"""
def f(x):
    while '2222' in x or '8888' in x:
        if '2222' in x:
            x = x.replace('2222', '88', 1)
        else:
            x = x.replace('8888', '22', 1)
    return x
print(f('8'*70))