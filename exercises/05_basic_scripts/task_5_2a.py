# -*- coding: utf-8 -*-
"""
Task 5.2a

Copy and modify the script from task 5.2 so that, if the user entered a host address
rather than a network address, convert the host address to a network address
and print the network address and mask, as in task 5.2.

An example of a network address (all host bits are equal to zero):
* 10.0.1.0/24
* 190.1.0.0/16

Host address example:
* 10.0.1.1/24 - host from network 10.0.1.0/24
* 10.0.5.195/28 - host from network 10.0.5.192/28

If the user entered the address 10.0.1.1/24, the output should look like this:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different host/mask combinations, for example:
    10.0.5.195/28, 10.0.1.1/24

Hint:
The network address can be calculated from the binary host address and the netmask.
If the mask is 28, then the network address is the first 28 bits host addresses + 4 zeros.
For example, the host address 10.1.1.195/28 in binary will be:
bin_ip = "00001010000000010000000111000011"

Then the network address will be the first 28 characters from bin_ip + 0000
(4 because in total there can be 32 bits in the address, and 32 - 28 = 4)
00001010000000010000000111000000

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
ip = input('Please, enter IP and Mask in CIDR notation: ')
iplist = ip.split('/')
ip_cidr = iplist[0].split('.')
mask_cidr = int(iplist[1])
mask_bin = '1' * mask_cidr + '0' * (32-mask_cidr)
mask_oct1, mask_oct2, mask_oct3, mask_oct4 = [
    int(mask_bin[:8], 2),
    int(mask_bin[8:16], 2),
    int(mask_bin[16:24], 2),
    int(mask_bin[24:], 2)
    ]

oct1, oct2, oct3, oct4 = [
    int(ip_cidr[0]),
    int(ip_cidr[1]),
    int(ip_cidr[2]),
    int(ip_cidr[3])
]

ip_bin = '{:08b}{:08b}{:08b}{:08b}'.format(oct1, oct2, oct3, oct4)
network_bin = ip_bin[:mask_cidr] + '0' * (32-mask_cidr)

net1, net2, net3, net4 = [
    int(network_bin[:8], 2),
    int(network_bin[8:16], 2),
    int(network_bin[16:24], 2),
    int(network_bin[24:], 2)
]


print(f'Network:\n'
      f'{net1:<8}  {net2:<8}  {net3:<8}  {net4:<8}\n'
      f'{net1:08b}  {net2:08b}  {net3:08b}  {net4:08b}\n\n'
      f'Mask:\n/{mask_cidr}\n'
      f'{mask_oct1:<8}  {mask_oct2:<8}  {mask_oct3:<8}  {mask_oct4:<8}\n'
      f'{mask_oct1:08b}  {mask_oct2:08b}  {mask_oct3:08b}  {mask_oct4:08b}\n')
