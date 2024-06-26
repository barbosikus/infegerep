"""
Алгоритм вычисления функции F(n) задан следующими соотношениями:

F(n) = n + 3                  при n <= 18
F(n) = (n//3)F(n//3) + n − 12 при n >  18 кратных 3
F(n) = F(n−1) + n² + 5        при n >  18 не кратных 3

Здесь «//» обозначает деление нацело. Определите количество натуральных
значений n из отрезка [1; 1000] для которых все цифры значения F(n) чётные.
"""
def f(n):
    if n<=18:
        return n+3
    if n>18 and n%3==0:
        return (n//3)*f(n//3)+n-12
    if n > 18 and n % 3 != 0:
        return f(n-1)+n**2 +5
c = 0

for i in range(1,1001):
    s = f(i)
    if all(int(d)%2==0 for d in str(s)):
        c+=1
print(c)
