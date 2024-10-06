n, q = map(int, input().split())
s1,c1,s2,c2 = map(int, input().split())
A,B = map(int, input().split())
a = 2*x*z -A*B
b = 2*y*z
m = float('+inf')
if s1>=(a+b):
    m = min((a+b)*c1, m)
if s2>=(a+b):
    m = min((a+b)*c2, m)
if s1>=a and s2>=b:
    m = min(a*c1 + b*c2, m)
if s2>=a and s1>=b:
    m = min(a*c2 + b*c1, m)
a = 2*x*z
b = 2*y*z-A*B
if s1>=(a+b):
    m = min((a+b)*c1, m)
if s2>=(a+b):
    m = min((a+b)*c2, m)
if s1>=a and s2>=b:
    m = min(a*c1 + b*c2, m)
if s2>=a and s1>=b:
    m = min(a*c2 + b*c1, m)
if m == float('+inf') or B>z or (A>x and A>y):
    print(-1)
else:
    print(m,a*c2 + b*c1)
print(m,a*c2 + b*c1, (A<=x and A<=y))
