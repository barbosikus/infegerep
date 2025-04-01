from turtle import *
tracer(0)
seth(90)
m = 10
for i in range(9):
    fd (7*m)
    rt(90)
    fd(42*m)
    rt(90)
pu()
bk(10*m)
lt(90)
bk(16*m)
pd()
for i in range(9):
    fd(42*m)
    rt(90)
    fd(16*m)
    rt(90)
pu()
for x in range(-10,100):
    for y in range(-10, 100):
        goto(x*m, y*m)
        dot(3, 'red')
mainloop()