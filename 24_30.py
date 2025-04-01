a = open('24_3099.txt').readline()
arr = [a.count(chr(i)) for i in range(ord('A'), ord('Z')+1)]
c = 0
for i in arr:
    if i%2!=0:
        c+=1
print(c//2)