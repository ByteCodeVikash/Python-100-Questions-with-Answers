import re 

def is_valid_mac_address(mac):
    mac_pattern=re.compile(r"""
        (^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$) |  # Pattern with colons or hyphens
        (^([0-9A-Fa-f]{2}){6}$)                        # Pattern without any separators
    """, re.VERBOSE)

    return bool(mac_pattern.match(mac))

test_cases=[
        "00:1A:2B:3C:4D:5E",  # valid
    "00-1A-2B-3C-4D-5E",  # valid
    "001A2B3C4D5E",       # valid
    "00:1A:2B:3C:4D:5Z",  # invalid (Z is not a valid hexadecimal digit)
    "00:1A:2B:3C:4D",     # invalid (too short)
    "00:1A:2B:3C:4D:5E:6F" # invalid (too long)

]

for mac in test_cases:
    print(mac,"is valid",is_valid_mac_address(mac))