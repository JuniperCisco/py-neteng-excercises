# -*- coding: utf-8 -*-
"""
Task 4.8

Convert the IP address in the ip variable to binary and print output in columns
to stdout:
- the first line must be decimal values
- the second line is binary values

The output should be ordered in the same way as in the example output below:
- in columns
- column width 10 characters (in binary
  you need to add two spaces between columns
  to separate octets among themselves)

Example output for address 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Restriction: All tasks must be done using the topics covered in this and previous chapters.

Warning: in section 4, the tests can be easily "tricked" into making the
correct output without getting results from initial data using Python.
This does not mean that the task was done correctly, it is just that at
this stage it is difficult otherwise test the result.
"""

ip = "192.168.3.1"
oct1 = int(ip.split('.')[0])
oct2 = int(ip.split('.')[1])
oct3 = int(ip.split('.')[2])
oct4 = int(ip.split('.')[3])
decibin = f'''
{oct1:<8}  {oct2:<8}  {oct3:<8}  {oct4:<8}
{oct1:08b}  {oct2:08b}  {oct3:08b}  {oct4:08b}
'''
print(decibin)
