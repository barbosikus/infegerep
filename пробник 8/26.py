f = sorted([int(q) for q in open('26.txt')][1:])
c = []
cr = []
ir = 1
l = 0
for i in range(len(f)):
    if l!=ir:
        l+=1
        cr.append(f[i])
    else:
        cr.append(f[i])
        c.extend(cr)
        cr = []
        l = 0
        ir += 1
print(ir, sum(cr))
