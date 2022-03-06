# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
'''
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
'''