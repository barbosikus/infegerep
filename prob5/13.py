"""
В терминологии сетей TCP/IP маской сети называют двоичное число, 
которое показывает, какая часть IP-адреса узла сети относится к 
адресу сети, а какая — к адресу узла в этой сети. Адрес сети 
получается в результате применения поразрядной конъюнкции к 
заданному адресу узла и маске сети.

Сеть задана IP-адресом 212.192.32.96 и маской сети 255.255.255.224.

Сколько в этой сети IP-адресов компьютеров, в которых в правом байте 
нет комбинации из подряд идущих трёх единиц или трёх нулей?
"""
from itertools import *
c=0
for z in product("10", repeat=5):
    s = ''.join(z)
    if '000' not in s or '111' not in s:
        c+=1
print(c)