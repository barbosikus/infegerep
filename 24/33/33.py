"""
Текстовый файл состоит не более чем из 106 символов X, Y и Z.

Сколько раз в файле встречается последовательность символов XXXX?
"""
f = open('33.txt')
a = f.readline()
while 'XXXXX' in a:
    a = a.replace('XXXXX','XXXX XXXX')
print(a.count('XXXX'))