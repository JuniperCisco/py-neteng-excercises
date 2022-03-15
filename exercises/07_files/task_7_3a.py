# -*- coding: utf-8 -*-
"""
Task 7.3a

Make a copy of the code from the task 7.3.

Add this functionality: Sort output by VLAN number

As a result, you should get the following output:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Pay attention to vlan 1000 - it should be displayed last.
Correct sorting can be achieved if vlan is a number, not a string.

Hint: For sorting, it is convenient to first create a list of lists,
and then sort:

[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]

The sort must be by the first element (vlan), and if the first element is the same,
then the second. This is how the sorted function and the sort method work by default,
if you sort list of lists above.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""


mac_table = []

with open("CAM_table.txt") as conf:
    for line in conf:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, interface = words
            mac_table.append([int(vlan), mac, interface])

for vlan, mac, interface in sorted(mac_table):
    print(f"{vlan:<9}{mac:20}{interface}")


'''
My own solution (imperfect, columns not aligned properly)

mac_list = []

with open('CAM_table.txt') as f:
    for line in f:
        if '.' in line:
            mac_list.append(line.replace('DYNAMIC', '').rstrip().split())
            for i in mac_list:
                i[0] = int(i[0])
            mac_list = sorted(mac_list)
            for i in mac_list:
                i[0] = str(i[0])
                print(' '.join(i))


'''