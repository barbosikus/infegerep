"""
Найдите десятичное число x, такое что 20 < x < 30, запись которого
в системе счисления с основанием 3 заканчивается на 11.
"""
def tri(x):
    t = ''
    while x>0:
        t+=str(x%3)
        x//=3
    t = t[::-1]
    return t

for x in range(21,30):
    if tri(x)[-2:] == '11':
        print(x)
def tri(x):
    # x=переданное
    t = ''
    while x > 0:
        t += str(x % 3)
        x //= 3
    return t[::-1]

for i in range(21, 30):
    if tri(i)[-2:] == '11':
        print(i)