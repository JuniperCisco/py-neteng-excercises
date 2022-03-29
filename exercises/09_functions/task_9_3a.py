# -*- coding: utf-8 -*-
"""
Task 9.3a

Make a copy of the code from the task 9.3.

Add this functionality: add support for configuration when the port is in VLAN 1
and the access port setting looks like this:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

In this case, information should be added to the dictionary that the port in VLAN 1
Dictionary example:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw2.txt file.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""


def get_int_vlan_map(config_filename):
    """returns a tuple of two dictionaries:
* a dictionary of ports in access mode, where the keys are port numbers,
  and the access VLAN values (numbers):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
  'FastEthernet0/16': 17}
* a dictionary of ports in trunk mode, where the keys are port numbers,
  and the values are the list of allowed VLANs (list of numbers):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}"""
    acc_dict = {}
    trunk_dict = {}
    with open(config_filename) as f:
        for line in f:
            if line.startswith('interface'):
                intf = line.split()[-1]
            elif "access vlan" in line:
                acc_dict[intf] = int(line.split()[-1])
            elif "mode access" in line and "access vlan" not in line:
                acc_dict[intf] = 1
            elif "trunk allowed" in line:
                trunk_dict[intf] = [int(v) for v in line.split()[-1].split(',')]
        return acc_dict, trunk_dict


a = get_int_vlan_map('config_sw2.txt')
print(a)
