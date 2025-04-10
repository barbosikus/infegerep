"""
Автомат обрабатывает натуральное число N по следующему алгоритму:

1. Строится двоичная запись числа N.
2. Если N четное, то в конец полученной записи (справа) дописывается 0,
   в начало – 1; если N – нечётное в конец и начало дописывается по
   две единицы.
3. Результат переводится в десятичную систему и выводится на экран.

Пример. Дано число N = 13. Алгоритм работает следующим образом:
1. Двоичная запись числа N: 1101.
2. Число нечетное, следовательно по две единицы по краям – 11110111.
3. На экран выводится число 247.

Укажите наименьшее число, большее 52, которое может являться
результатом работы автомата.
"""
a = []
for n in range(1, 100):
    b = bin(n)[2:]
    b = '1' + b + '0' if n % 2 == 0 else '11' + b + '11'
    if int(b, 2) > 52 and int(b, 2) not in a:
        a.append(int(b, 2))
print(min(a))