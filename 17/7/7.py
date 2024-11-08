"""
В файле содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от –10 000 до
10 000 включительно. Определите и запишите в ответе сначала
количество пар элементов последовательности, произведение
которых положительно, а сумма кратна 7, затем минимальное из
произведений элементов таких пар. В данной задаче под парой
подразумевается два идущих подряд элемента последовательности.
"""
f = [int(q) for q in open('7.txt')]
c = 0
a = []
for i,j in zip(f,f[1:]):
    if i*j>0 and (i+j) % 7==0:
        c+=1
        a.append(i*j)
print(c,min(a))