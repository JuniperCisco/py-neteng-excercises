# -*- coding: utf-8 -*-
"""
Task 4.6

Process the ospf_route string and print the information to the stdout as follows:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
prefix = ospf_route.split()[0]
ad = ospf_route.split()[1].strip('[]')
nh = ospf_route.split()[3].strip(',')
lupdate = ospf_route.split()[4].strip(',')
iface = ospf_route.split()[5]
template = f'''
Prefix                {prefix}
AD/Metric             {ad}
Next-Hop              {nh}
Last update           {lupdate}
Outbound Interface    {iface}
'''
print(template)