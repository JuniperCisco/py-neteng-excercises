# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

The message "Invalid IP address" should be printed only once,
even if several chacks are not passed.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
while True:
    ip = input("Please, enter an IP address: ")
    octets = ip.split(".")
    valid_ip = len(octets) == 4

    for i in octets:
        valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip
    if valid_ip:
        break
    print('Invalid IP address.')

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

