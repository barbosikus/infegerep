"""
У исполнителя Калькулятор есть три команды, которым присвоены номера:

1. Прибавить 2
2. Прибавить 4
3. Прибавить 5

Определите число,
для получения которого из числа 31 существует 1001 программа.
"""
f = lambda x,y: 0 if x>y else 1 if x == y else f(x+2,y)+f(x+4,y)+f(x+5,y)
for y in range(1,1000):
    if f(31,y) == 1001:
        print(y)