"""
Исполнитель Калькулятор преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:

1. Прибавь 1
2. Прибавь 2
3. Умножь на 2

Первая команда увеличивает число на экране на 1,
вторая увеличивает его на 2,
третья – умножает на 2.

Программа для исполнителя – это последовательность команд.

Сколько существует программ,
которые преобразуют исходное число 1 в число 15
и при этом не содержат двух команд умножения подряд?
"""
f = lambda x,fl: 0 if x>15 else 1 if x == 15 else f(x+1,0)+f(x+2,0)+(f(x*2,1) if fl==0 else 0)
print(f(1,0))