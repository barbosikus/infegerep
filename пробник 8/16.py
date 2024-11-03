import sys
sys.setrecursionlimit(10000)
def f(n):
    if n<5:
        return 4**4
    else:
        return 4*f(n-4)+4
print(f(4048)/f(4036))