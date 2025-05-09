"""
В файле содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от –10 000
до 10 000 включительно. Определите и запишите в ответе сначала
количество троек элементов последовательности, в которых
произведение кратно 7, а сумма оканчивается на 5, затем
максимальную из сумм элементов таких троек. В данной задаче
под тройкой подразумевается три идущих подряд элемента
последовательности.
"""
f = [int(q) for q in open('8.txt')]
c = 0
a = []
for i,j,k in zip(f,f[1:],f[2:]):
    if (i*j*k)%7==0 and (i+j+k)%10==5:
        c+=1
        a.append(i+j+k)
print(c,max(a))

