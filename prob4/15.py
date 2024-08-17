"""
Для какого наименьшего целого неотрицательного числа A выражение

(3x+y>A)∧(y<x)∧(x<30)

тождественно ложно, т. е. принимает значение 0 при любых целых
неотрицательных x и y?
"""
from itertools import *
for a in range(1,10000):
    if all(not((3*x +y>a)and(y<x)and(x<30)) for x,y in product(range(1,10000), repeat = 2)):
        print(a)
