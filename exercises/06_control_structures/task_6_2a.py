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

'''MY VERSION'''
'''
ip = input('Please, enter an IP address: ')
octets = ip.split('.')
if len(octets) == 4 and octets[0].isdigit() and octets[1].isdigit() and octets[2].isdigit() and octets[
    3].isdigit() and 0 <= int(octets[0]) <= 255 and 0 <= int(octets[1]) <= 255 and 0 <= int(
        octets[2]) <= 255 and 0 <= int(octets[3]) <= 255:
    result = True
else:
    result = False
    
if result:
    if ip == '0.0.0.0':
        print('unassigned')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif 1 <= int(ip.split('.')[0]) <= 223:
        print('unicast')
    elif 224 <= int(ip.split('.')[0]) <= 239:
        print('multicast')
    else:
        print('unused')
else:
    print('Invalid IP address')
'''

'''@natenka version 1'''

ip = input("Please, enter an IP address: ")
octets = ip.split(".")
valid_ip = len(octets) == 4

for i in octets:
    valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

if valid_ip:
    if ip == '0.0.0.0':
        print('unassigned')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif 1 <= int(octets[0]) <= 223:
        print('unicast')
    elif 224 <= int(octets[0]) <= 239:
        print('multicast')
    else:
        print('unused')
else:
    print('Invalid IP address')