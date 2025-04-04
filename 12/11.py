"""
Чертёжник находился в начале координат. Ему был дан для исполнения
следующий алгоритм:

Сместиться на (-7,–1)
Повтори N раз
   Сместиться на (15, 22)
   Сместиться на (a, b)
конец
Сместиться на (23, –32)

Найдите наибольшее число повторений N в конструкции «Повтори … раз»,
при котором значения a и b можно выбрать так, что после выполнения
алгоритм Чертёжник окажется в точке (1; –3).
"""

from turtle import *
tracer(0)

for i in range(0, 100):
    for a in range(-20, 20):
        for b in range(-20, 20):
            goto(-7, -1)
            for n in range(0, i):
                        goto(xcor() + 15, ycor() + 22)
                        goto(xcor() + a, ycor() + b)
            goto(xcor() + 23, ycor() - 32)
            if xcor() == 1 and ycor() == -3:
                print(xcor(), ycor(), i,a,b)