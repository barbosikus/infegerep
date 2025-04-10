"""
Исполнитель преобразует число на экране.
У исполнителя есть две команды, которым присвоены номера:

1. Прибавить 1
2. Умножить на 2

Первая команда увеличивает число на экране на 1,
вторая умножает его на 2.

Программа для исполнителя – это последовательность команд.

Сколько существует программ,
для которых при исходном числе 1 результатом является число 30,
при этом траектория вычислений проходит через 12?

Траектория вычислений программы –
это последовательность результатов выполнения всех команд программы.

Например, для программы 121 при исходном числе 7
траектория будет состоять из чисел 8, 16, 17.
"""
def f(x,y):
    if x>y:
        return 0
    if x == y:
        return 1
    return f(x+1,y)+f(x*2,y)
print(f(1,12)*f(12,30))