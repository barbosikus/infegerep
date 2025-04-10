"""
Входной файл содержит сведения о ставках 
на электронном закрытом аукционе по продаже антиквариата. 
Аукцион проводится по правилу второй цены: товар получает 
тот, кто сделал самую большую ставку, но по цене второй по 
величине ставки. Если ставок меньше двух, то лот остаётся 
непроданным. Каждый участник делает любое количество заявок 
на любые лоты.

Определите количество проданных лотов и общую стоимость 
всех проданных лотов.

Входные данные

В первой строке входного файла находится три натуральных числа: 
L (1≤L≤1000) — количество лотов, P (1≤P≤1000) — количество 
участников и N (1≤N≤10000) — число заявок.

Следующие N строк содержат номер лота, номер участника и ставку. 
Запишите в ответе два числа: количество проданных лотов и общую 
стоимость всех проданных лотов.

Типовой пример организации данных во входном файле

5 3 6
1 1 10
1 2 15
3 3 3
4 3 10
4 3 7
5 1 5

При таких исходных данных лот 1 продан участнику 2 по 
цене 10, лоты 2, 3 и 5 не проданы, лот 4 продан 
участнику 3 по цене 7. В итоге проданы лоты 1 и 4 с 
общей стоимостью 10+7=17. Ответ: 2 17
"""
f = open('26.txt')
L, p, n = map(int, f.readline().split())
l = [[]]*L
c = 0
j = 0
for i in range(n):
    l1, _, n1 = map(int, f.readline().split())
    l[l1].append(n1)
for i in l:
    if len(i)>1:
        c += sorted(set(i))[-2]
        j+=1
print(c, j)