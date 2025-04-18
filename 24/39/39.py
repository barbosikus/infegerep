"""
Текстовый файл состоит не более чем из 106 заглавных латинских букв (A..Z).
Текст разбит на строки различной длины.

Определите количество строк,
в которых комбинация букв AOA встречается чаще комбинации OAO.
"""
f = open('39.txt')
a = f.readlines()
e = 0
for i in a:
    c1=0
    c2=0
    for a,b,c in zip(i,i[1:], i[2:]):
        if a+b+c=='OAO':
            c1+=1
        if a+b+c=='AOA':
            c2+=1
    if c2>c1:
        e+=1
print(e)