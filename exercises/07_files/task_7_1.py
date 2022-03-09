# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

with open('ospf.txt') as ospf_file:
    for line in ospf_file:
        prefix = line.rstrip().split('\n')[0].split()[1]
        ad = line.rstrip().split('\n')[0].split()[2].strip('[]')
        nhop = line.rstrip().split('\n')[0].split()[4].strip(',')
        lupd = line.rstrip().split('\n')[0].split()[5].strip(',')
        intf = line.rstrip().split('\n')[0].split()[6].strip(',')
        print(f'''
Prefix                {prefix}
AD/Metric             {ad}
Next-Hop              {nhop}
Last update           {lupd}
Outbound Interface    {intf}
''')




