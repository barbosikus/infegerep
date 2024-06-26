"""
Исполнитель Черепаха действует на плоскости с декартовой системой
координат. В начальный момент Черепаха находится в начале координат,
её голова направлена вдоль положительного направления оси ординат,
хвост опущен. При опущенном хвосте Черепаха оставляет на поле
след в виде линии. В каждый конкретный момент известно положение
исполнителя и направление его движения. У исполнителя существует
две команды:

    Вперёд n (где n–целое число), вызывающая передвижение Черепахи
    на n единиц в том направлении, куда указывает её голова,

    Направо m (где m– целое число), вызывающая изменение направления
    движения на m градусов по часовой стрелке.

Запись Повтори k [Команда1 Команда2 … КомандаS] означает,
что последовательность из S команд повторится k раз.

Черепахе был дан для исполнения следующий алгоритм:

    Повтори 15 [ Вперёд 7 Направо 30 Вперёд 8 Направо 150].

Определите площадь получившейся фигуры в квадратных единицах.
"""
from turtle import *
home()
seth(90)
tracer(0)
r = 20
for i in range(15):
    fd(7*r)
    right(30)
    fd(8*r)
    right(150)
update()
mainloop()
'''s = sin30 * 8 * 7 = 28'''