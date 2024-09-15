"""
Алгоритм вычисления значения функции F(n), где 
n — натуральное число, задан следующими соотношениями:

F(n)=1 при n≥2024,
F(n)=F(n+2)+F(n+4) в остальных случаях.

Сколько различных натуральных чисел в области 
значений функции F(n)?
"""
import sys
from functools import *
sys.setrecursionlimit(100000)
@lru_cache(None)

def f(n):
    if n>=2024:
        return 1
    else:
        return f(n+2)+f(n+4)
c = []
for n in range(5000):
    c.append(f(n))
c = set(c)
print(len(c))
'1014'