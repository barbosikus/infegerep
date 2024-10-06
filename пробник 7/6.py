from turtle import *
home()
tracer(0)
seth(90)
r = 20
for i in range(9):
    fd(r*22)
    rt(90)
    fd(r * 6)
    rt(90)
pu()
fd(r*1)
rt(90)
fd(r*5)
left(90)
pd()
for i in range(9):
    fd(r * 53)
    rt(90)
    fd(r * 75)
    rt(90)
pu()
for x in range(-20, 20):
    for y in range(-20,30):
        goto(x*r, y*r)
        dot(3, 'red')
mainloop()