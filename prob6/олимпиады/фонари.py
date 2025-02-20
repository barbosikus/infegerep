x,y,k,l = map(int, input().split())
if (y-x)%k==0:
    if (k-2*l)%(2*l)==0:
        print((abs(y-x)//k)*((k-2*l)//(2*l)))
    else:
        print((abs(y - x) // k) * (((k - 2 * l) // (2 * l))+1))
else:
    if x%k == 0 and y%k==0:
        if (k - (2 * l)) % (2 * l) == 0:
            print((abs(y - x) // k +3) * ((k - 2 * l) // (2 * l)))
        else:
            print(((abs(y - x) // k) + 3) * ((k - 2 * l) // (2 * l) + 1))
    if x%k == 0 and y%k!=0 or y%k == 0 and x%k!=0:
        if (k - (2 * l)) % (2 * l) == 0:
            print((abs(y - x) // k +2) * ((k - 2 * l) // (2 * l)))
        else:
            print(((abs(y - x) // k) + 2) * ((k - 2 * l) // (2 * l) + 1))
    else:
        if (k - (2 * l)) % (2 * l) == 0:
            print((abs(y - x) // k +1) * ((k - 2 * l) // (2 * l)))
        else:
            print(((abs(y - x) // k) + 1) * ((k - 2 * l) // (2 * l) + 1))