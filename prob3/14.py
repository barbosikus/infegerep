"""
Определите количество ненулевых цифр в девятеричной записи числа

2 ⋅ 729^333 + 2 ⋅ 243^334 − 81^335 + 2 ⋅ 27^336 − 2 ⋅ 9^337 − 338 
"""
n = 2 * 729**333 + 2 *243**334 - 81**335 + 2 * 27**336 - 2 * 9**337 - 338
n9 = ''
while n>0:
    n9 += str(n%9)
    n = n//9
    n9 = n9[::-1]
n9 = n9.replace('0', '')
print(len(n9), n9)