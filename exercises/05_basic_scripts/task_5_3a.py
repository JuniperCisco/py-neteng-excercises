# -*- coding: utf-8 -*-
"""
Task 5.3a

Copy and change the script from task 5.3 in such a way that, depending on
the selected mode, different questions were asked in the request for the VLAN number
or VLAN list:
* for access: 'Enter VLAN number:'
* for trunk: 'Enter the allowed VLANs:'

Restriction: All tasks must be done using the topics covered in this and previous chapters.
This task can be solved without using the if condition and for/while loops.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
template_dict = {
    'access': access_template,
    'trunk': trunk_template
}
vlan_prompt_dict = {
    'access': 'Enter VLAN number: ',
    'trunk': 'Enter the allowed VLANs: '
}
iface_mode = input('Enter interface mode (access/trunk): ')
iface_number = input('Enter interface type and number: ')
iface_vlans = input(vlan_prompt_dict[iface_mode])


print('interface ' + iface_number)
print('\n'.join(template_dict[iface_mode]).format(iface_vlans))
