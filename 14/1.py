"""
Значение арифметического выражения: 64³⁰ + 2³⁰⁰ – 4 записали в
системе счисления с основанием 8. Сколько цифр «7» в этой записи?
"""
n = oct(64**30 + 2**300 - 4)[2:]
print(n.count('7'))
