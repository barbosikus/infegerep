"""
Автомат обрабатывает натуральное число N по следующему алгоритму:

1. Строится двоичная запись числа N.
2. Складываются все цифры полученной двоичной записи.
   В конец записи (справа) дописывается остаток от деления полученной
   суммы на 2.
3. Предыдущий пункт повторяется для записи с добавленной цифрой.
4. Результат переводится в десятичную систему и выводится на экран.

Сколько различных чисел, меньших 80, могут появиться на экране в
результате работы автомата?
"""
c = 0
for n in range(1, 100):
    b = bin(n)[2:]
    s = b. count('1')
    for i in range(2):
        b+= str(s%2)
    if int(b, 2) < 80:
        c+=1
print(c)