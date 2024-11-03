from turtle import *
tracer(0)
home()
seth(90)
r = 15
for i in range(2):
    fd(11*r)
    right(90)
    fd(17 * r)
    right(90)
pu()
fd(7 * r)
left(90)
back(1*r)
right(90)
pd()
for i in range(2):
    fd(15 * r)
    right(90)
    fd(7 * r)
    right(90)
pu()
for x in range(-20,20):
    for y in range(-20,20):
        goto(x*r, y*r)
        dot(3, 'red')
mainloop()