# -*- coding: utf-8 -*-
"""
Task 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), print to the stdout:
    'unicast' - if the first byte is in the range 1-223
    'multicast' - if the first byte is in the range 224-239
    'local broadcast' - if the IP address is 255.255.255.255
    'unassigned' - if the IP address is 0.0.0.0
    'unused' - in all other cases

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip = input('Please, enter an IP address: ')
if ip == '0.0.0.0':
    print('unassigned')
elif ip == '255.255.255.255':
    print('local broadcast')
elif int(ip.split('.')[0]) <= 223:
    print('unicast')
elif int(ip.split('.')[0]) <= 239:
    print('multicast')
else:
    print ('unused')