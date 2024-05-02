"""
Чертежнику был дан для исполнения следующий алгоритм:

Сместиться на (3,–6)
Повтори N раза
   Сместиться на (4, b)
   Сместиться на (6, –6)
конец
Сместиться на (-53, 26)

Найдите целое значение b, для которого после выполнения программы
Чертёжник окажется в исходной точке.
"""

from itertools import product as p
from turtle import xcor as x, ycor as y

from turtle import *
# tracer(0)
r = 10
for i in range(100):
    fd(10)
    rt(8)
tracer(0)
goto(-200, -200)
update()
exitonclick()
for x in range(-200,200):
    for y in range(-200, 200):
        goto(x*r, y*r)
        dot(3, 'blue')
# update()
# def f(b, n):
#     goto(3,-6)
#     for i in range(n):
#         goto(x() + 4, y() + b)
#         goto(x() + 6, y() - 6)
#     goto(x() - 53, y() + 26)
#
# for n in range(0,100):
#     for b in range(0, 50):
#         f(b, n)
#         if x() == 0 and y() == 0:
#             print(b, n)
#     print(n)