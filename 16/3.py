"""
Алгоритм вычисления функции F(n) задан следующими соотношениями:

F(n) = n              при n <= 10
F(n) = n//4 + F(n−10) при 10 < n <= 36
F(n)=2⋅F(n−5)         при n>36

Здесь // обозначает деление нацело. В качестве ответа на задание
выведите значение F(100).
"""
def f(n):
    if n<=10:
        return n
    if 10<n<=36:
        return n//4 + f(n-10)
    if n>36:
        return 2*f(n-5)
print(f(100))