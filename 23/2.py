"""
У исполнителя Калькулятор три команды, которым присвоены номера:

1. прибавь 1
2. умножь на 2
3. возведи в квадрат

Сколько есть программ,
которые число 5 преобразуют в число 154?
"""
def f(x):
    if x >154:
        return 0
    if x == 154:
        return 1
    return f(x+1)+f(x*2)+f(x**2)
print(f(5))