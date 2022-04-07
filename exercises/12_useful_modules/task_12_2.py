# -*- coding: utf-8 -*-
"""
Task 12.2

The ping_ip_addresses function from task 12.1 only accepts a list of addresses,
but it would be convenient to be able to specify addresses using a range,
for example 192.168.100.1-10.

In this task, you need to create a function convert_ranges_to_ip_list that
converts a list of IP addresses in different formats into a list where each
IP address is listed separately.

The function expects as an argument a list containing IP addresses
and/or ranges of IP addresses.

List items can be in the format:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

If the address is specified as a range, the range must be expanded into
individual addresses, including the last address in the range.
To simplify the task, we can assume that only the last octet of the
address changes in the range.

The function returns a list of IP addresses.

For example, if you pass the following list to the convert_ranges_to_ip_list function:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

The function should return a list like this:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""


def convert_ranges_to_ip_list(ip_range):
    final_ip_list = []
    for ip in ip_range:
        conv_ip = ip.split('-')
        if '-' in ip:
            octets = conv_ip[0].split('.')
            if '.' not in conv_ip[1]:
                last_octet = conv_ip.pop(-1)
                for i in range(int(octets[3]), (int(last_octet)+1)):
                    final_ip_list.append(f'{octets[0]}.{octets[1]}.{octets[2]}.{i}')
            else:
                last_octet = conv_ip[-1].split('.').pop(-1)
                for i in range(int(octets[3]), (int(last_octet) + 1)):
                    final_ip_list.append(f'{octets[0]}.{octets[1]}.{octets[2]}.{i}')
        else:
            final_ip_list.append(ip)
    return final_ip_list


#a = convert_ranges_to_ip_list(['1.1.1.1', '10.0.0.0-2', '2.2.2.2', '10.1.1.0-10.1.1.3'])
#print(a)
