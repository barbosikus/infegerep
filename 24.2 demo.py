import re
a = open('24 demo').readline()
def f(x):
    return bool(re.match(r'^(?!0[6-9])([6-9][06789]*|0)([-*](?!0[6-9])([6-9][06789]*|0))*$', x))
c = []
for l in range(len(a),0,-1):
    for i in range(len(a)-l+1):
        s = a[i:i+l]
        print(s)
        if f(s):
            c.append(l)
            print(max(c))
            break

