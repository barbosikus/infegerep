"""
У исполнителя Калькулятор две команды, которым присвоены номера:

1. прибавь 1
2. увеличь каждый разряд числа на 1

Например, число 23 с помощью команды 2 превратится в 34,
а 29 в 39 (так как младший разряд нельзя увеличить).

Если перед выполнением команды 2 какая-либо цифра равна 9,
она не изменяется.

Сколько есть программ,
которые число 25 преобразуют в число 51?
"""
def y(x):
    if x//10 !=9:
        x+=10
    if x%10!=9:
        x+=1
    return x



def f(x):
    if x>51:
        return 0
    if x == 51:
        return 1
    return f(x+1)+f(y(x))
print(f(25))