# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
ip = input('Please, enter IP and Mask in CIDR notation: ')
iplist = ip.split('.')
oct1 = int(iplist[0])
oct2 = int(iplist[1])
oct3 = int(iplist[2])
oct4 = int(iplist[3].split('/')[0])
mask_cidr = int(iplist[3].split('/')[1])
mask_octets = '1' * mask_cidr + '0' * (32-mask_cidr)
mask_oct1 = int(mask_octets[:8], 2)
mask_oct2 = int(mask_octets[8:16], 2)
mask_oct3 = int(mask_octets[16:24], 2)
mask_oct4 = int(mask_octets[24:], 2)

print(f'Network:\n'
      f'{oct1:<8}  {oct2:<8}  {oct3:<8}  {oct4:<8}\n'
      f'{oct1:08b}  {oct2:08b}  {oct3:08b}  {oct4:08b}\n\n'
      f'Mask:\n/{mask_cidr}\n'
      f'{mask_oct1:<8}  {mask_oct2:<8}  {mask_oct3:<8}  {mask_oct4:<8}\n'
      f'{mask_oct1:08b}  {mask_oct2:08b}  {mask_oct3:08b}  {mask_oct4:08b}\n')

''' 
This is how @natenka did it:

ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_output = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_output.format(oct1, oct2, oct3, oct4))
print(mask_output.format(mask_cidr, mask_oct1, mask_oct2, mask_oct3, mask_oct4))
'''