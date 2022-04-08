# -*- coding: utf-8 -*-
"""
Task 12.3

Create a function print_ip_table that prints a table of available
and unavailable IP addresses.

The function expects two lists as arguments:
* list of available IP addresses
* list of unavailable IP addresses

The result of the function is printing a table to the stdout:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9
"""


from tabulate import tabulate


def print_ip_table(available_ips, unavailable_ips):
    all_ips = {'Reachable': available_ips, 'Unreachable': unavailable_ips}
    print(tabulate(all_ips, headers='keys'))


if __name__ == '__main__':
    available_ips = ['10.1.1.1', '10.2.2.2']
    unavailable_ips = ['8.8.8.8', '1.1.1.1', '3.2.1.0']
    print_ip_table(available_ips, unavailable_ips)



