from itertools import *
for x,y,z,w in product((0,1), repeat = 4):
    if (w and (y == (z<=(x or y)))):
        print(w,x,y,z)