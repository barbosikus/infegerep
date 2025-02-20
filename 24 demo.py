a = open('24 demo').readline()
x = ['6','7','8','9']
ch = [*x, '0']
z = ['*', '-']
j = ch
c = 0
cnt = []
k = 1 #сигнализирует что предыдущий - знак
for i in range(len(a)):
    if a[i] in j:
        c+=1
        if a[i] == '0' and k == 1:
            k = 0
            j = z
        else:
            if a[i] in z:
                j = ch
                k = 1
            else:
                k = 0
                j = ch + z
        #print(a[i], end = '')
    else:
        j = ch
        c-=k
        cnt.append(c)
        c = 0
        #print()
print(max(cnt))