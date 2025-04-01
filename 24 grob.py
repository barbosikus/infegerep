a = open('24_19149.txt').readline()
ch = ['1', '2', '3', '4']
i = 0
posl = []
def f(x):
    y = x[1:-1].replace('(','').replace(')','').split('+')
    print(x)
    s = sum(map(int, y))
    if s%2==0:
        return len(x)
    else:
        return 0

def g(x, y):
    if x[y] == '(' and x[y + 1] != '+' and x[y + 1] != ')':
        b = '('
        y+=1
        while x[y] != ')':
            if x[y] == '(' and (x[y-1]=='+' or x[y-1] == '('):
                h = g(x,y)
                if h == '' or h == None:
                    return ''
                b += h
                y+=len(h)
            else:
                b += x[y]
                y += 1
                if x[y] == '(' and x[y - 1] != '+':
                    return ''
            if b[-1] == '+' and x[y] == '+':
                return ''
            if b[-1] == ')' and x[y] != '+':
                return ''

        if x[y] == ')' and x[y - 1] != '+' and b.count('+')>0:
            print(b)
            return b+')'
    return ''

while i<len(a):
    j = g(a, i)
    if j!='':
        posl.append(j)
    i+=1
print(posl)
print(max(posl, key = lambda a : f(a)))
