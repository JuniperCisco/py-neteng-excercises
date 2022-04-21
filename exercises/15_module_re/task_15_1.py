# -*- coding: utf-8 -*-
"""
Task 15.1

Create a get_ip_from_cfg function that expects the name of the file containing
the device configuration as an argument.

The function should process the configuration and return the IP addresses and
masks that are configured on the interfaces as a list of tuples:
* the first element of the tuple is the IP address
* the second element of the tuple is a mask

For example (arbitrary addresses are taken):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

To get this result, use regular expressions.

Check the operation of the function using the config_r1.txt file.

Please note that in this case, you can not check the correctness
of the IP address, address ranges, and so on, since the command
output from network device is processed, not user input.

"""


###
# Not the most elegant solution but it works, lol :D
###

import re


def get_ip_from_cfg(filename):
    result = []
    with open(filename) as f:
        try:
            for line in f:
                if 'ip address ' in line:
                    ip_mask = re.search("ip address (\S+) (\S+)", line).groups()
                    result.append(ip_mask)
                else:
                    pass
        except AttributeError:
            pass
    return result


if __name__ == '__main__':
    print(get_ip_from_cfg('config_r1.txt'))

###
# More elegant one
###

'''import re


def get_ip_from_cfg(config):
    regex = r"ip address (\S+) (\S+)"
    with open(config) as f:
        result = [m.groups() for m in re.finditer(regex, f.read())]
    return result'''