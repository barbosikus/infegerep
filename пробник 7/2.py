from itertools import *
for x,y,z,w in product((0,1), repeat = 4):
    if not(((w<=y)<=x) or not(z)):
        print(z,y,w,x)