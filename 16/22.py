"""
Алгоритм вычисления значения функции F(n), где n – натуральное число,
задан следующими соотношениями:

F(n)=1            при  n = 1;
F(n)=n² + F(n−1), если n > 1.

Чему равно значение выражения F(1 000)−F(997)?
"""
from sys import *
def f(n):
    if n == 1:
        return 1
    if n>1:
        return n**2+f(n-1)
setrecursionlimit(2000)
print(f(1000)-f(997))
print(getrecursionlimit())
print(1000**2+999**2+998**2)