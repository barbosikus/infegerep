from itertools import *
for x,y,z,w in product((0,1), repeat = 4):
    if not(y and (x or z) or not(y or z) or w):
        print(x,y,w,z)