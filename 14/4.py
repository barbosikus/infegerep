"""
Значение арифметического выражения: 51×7¹² – 7³ – 22 – записали
в системе счисления с основанием 7. Найдите сумму цифр в этой
записи? В ответе укажите найденную сумму как число в десятичной
системе счисления.
"""
n = 51*7**12 - 7**3 - 22
b = ''
c = 0
while n>0:
    b += str(n%7)
    n//=7
b = int(b[::-1])
print(b)
while b>0:
    c+= b%10
    b = b//10
print(c)

