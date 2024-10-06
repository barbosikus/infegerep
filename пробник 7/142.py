def f(x):
    b = ''
    while x>0:
        b+=str(x%25)
        x//=25
    b = b[::-1]
    return(b)
n = 3*3125**8+2*625**7- 4*625**6 + 3*125**5 - 2*25**4 - 2025
print(f(n).count('0'))