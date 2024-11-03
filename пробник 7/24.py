f = open('24.txt')
a = f.readline().replace('--','#').replace('**','#').replace('*-','#').replace('-*','#').replace('8','&').replace('6','&')\
.replace('7','&').replace('9','&').replace('-','*').split('#')


cg = 0
for i in a:
    c = [0]
    for j in range(len(i)):
        if j == 0:
            if i[j] == '0':
                for k in range(len(i)):
                    if i[k] == '*':
                        j = k
                        break
            else:
                c[-1]+=1
        else:
            if i[j-1] == '*' and i[j] == '0':
                for k in range(j, len(i)):
                    if i[k] == '*':
                        j = k
                        c[-1]-=1
                        c.append(0)
                        break
            else:
                c[-1]+=1
    cg = max(cg, max(c))
print(cg)

