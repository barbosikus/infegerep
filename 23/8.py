"""
Исполнитель R17 преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:

1. Прибавить 1
2. Прибавить 3
3. Умножить на 2

Программа для исполнителя R17 – это последовательность команд.

Сколько существует таких программ,
которые исходное число 3 преобразуют в число 20
и при этом траектория вычислений программы содержит число 9 и число 12?
"""
f = lambda x,y: 0 if x>y else 1 if x == y else f(x+1,y)+f(x+3,y)+f(x*2,y)
print(f(3,9)*f(9,12)*f(12,20))