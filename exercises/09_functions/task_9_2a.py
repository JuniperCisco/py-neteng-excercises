# -*- coding: utf-8 -*-
"""
Task 9.2a

Make a copy of the code from the task 9.2.

Change the function so that it returns a dictionary instead of a list of commands:
- keys: interface names, like 'FastEthernet0/1'
- values: the list of commands that you need execute on this interface

Check the operation of the function using the example of the trunk_config
dictionary and the trunk_mode_template template.

An example of a final dict (each string is written on a new line for readability):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
- intf_vlan_mapping: expects a dictionary with interface-VLAN mapping:
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
- trunk_template: expects trunk port configuration template as command list
  (trunk_mode_template list)

    Returns a list of commands.
    """
    trunk_dict = {}
    for intf, vlans in intf_vlan_mapping.items():
        commands_list = []
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                vlans_str = ','.join([str(vl) for vl in vlans])
                commands_list.append(f"{command} {vlans_str}")
            else:
                commands_list.append(command)
        trunk_dict[intf] = commands_list
    return trunk_dict

a = generate_trunk_config(trunk_config, trunk_mode_template)
print(a)