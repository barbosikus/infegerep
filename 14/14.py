"""
В какой системе счисления выполняется равенство 21ₓ · 13ₓ = 313ₓ?
В ответе укажите число – основание системы счисления.
"""
for x in range(4,32):
    if int('21',x) * int('13',x) == int('313', x):
        print(x)