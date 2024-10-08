"""
В файле содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от 0 до 10 000
включительно. Определите количество пар чисел, в которых ровно
один из двух элементов больше, чем сумма цифр всех чисел в файле,
делящихся на 35, а шестнадцатеричная запись другого оканчивается
на EF. В ответе запишите два числа: сначала количество найденных
пар, а затем – минимальную сумму элементов таких пар. В данной
задаче под парой подразумевается два идущих подряд элемента
последовательности.
"""
f = [int(q) for q in open('20.txt')]
a = sum([sum(map(int,str(a))) for a in f if a%35==0])
a1 = [a for a in f if a%35==0]
c = 0
b = []
for i,g in zip(f,f[1:]):
    if ((i>a and g<a) and hex(g)[-2]=="e" and hex(g)[-1]=="f") or ((i<a and g>a) and hex(i)[-2]=="e" and hex(i)[-1]=="f"):
        c+=1
        b.append(i+g)
print(c, min(b))
