"""
Текстовый файл содержит строку из заглавных букв A, B, C, D, E, F,
всего не более чем из 106 символов.

AF-подстроками назовём непустые последовательности идущих подряд символов
A, B, C, D, E, F, ограниченные в начале символом A,
а в конце символом F (граничные символы входят в подстроку).

Определите количество AF-подстрок длиной от 7 до 10 символов.
"""
f = open('40.txt')
a = f.readline()
ind = 0
t = []
while ind!=len(a):
    if a[ind]=='A':
        d = ''
        while a[ind]!='F' and ind!=len(a)-1:
            d+=a[ind]
            ind+=1
        t.append(d)
    ind+=1
c = 0
for i in t:
    if 7<=len(i)<=10:
        c+=1
print(c)