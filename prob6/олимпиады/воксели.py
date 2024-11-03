a = input()
b = input()
arr = []

def f(a, arr):
    c = 0
    i = 0
    while i<len(a):
        if a[i] == 'Q':
            arr.append([])
            i += f(a[i+1:], arr[-1])
        else:
            arr.append(a[i])
        c+=1
        i+=1
        if c == 8:
            return i
def g(b, arr, j):
    s = 0
    for i in range(len(arr)):
        if 'list' in str(type(arr[i])):
            s += g(b,arr[i], j//8)
        else:
            if b == arr[i]:
                print(s, j)
                s += j

    return s


j = 2**40
f(a, arr)
print(arr, int(bin(g(b, arr, j))[2:])/10**40)