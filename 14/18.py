"""
Запись числа N в системе счисления c основанием 6 содержит две цифры,
запись этого числа в системе счисления c основанием 5 содержит три цифры,
а запись в системе счисления c основанием 11 заканчивается на 1.
Чему равно N? Запишите ответ в десятичной системе счисления.
"""
def f(x, c):
    t = ''
    while x>0:
        t+= str(x%c)
        x//=c
    return t[::-1]


for n in range(1, 10000000):
    if len(f(n,6)) == 2 and len(f(n, 5)) == 3 and f(n, 11)[-1] == '1':
        print(n)
