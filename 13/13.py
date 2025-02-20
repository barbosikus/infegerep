from ipaddress import *

for i in range(24,32):
    s = ip_network(f'172.16.168.0/{i}',0)
    c = 0
    for j in range(1, int('1'*(32-i),2)):
        b = bin(j)[2:]
        d = b.count('0')
        #print(d)
        if (16+i-24+d)%7==0:
            c+=1
            print(c,j)
    if c == 35:
        print(i)