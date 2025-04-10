"""
В терминологии сетей TCP/IP маской сети называют двоичное число, которое
показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая –
к адресу узла в этой сети. Адрес сети получается в результате применения
поразрядной конъюнкции к заданному адресу узла и его маске.

Сеть задана IP-адресом 112.208.0.0 и сетевой маской 255.255.128.0.

Сколько в этой сети ІР-адресов, для которых количество единиц в двоичной
записи IP-адреса кратно 11? В ответе укажите только число.
"""
from ipaddress import *
net = ip_network('112.208.0.0/255.255.128.0',0)
b = ''
c = 0
for i in net:
    b = f'{i:b}'
    if b.count('1')%11==0:
        c+=1
print(c)

